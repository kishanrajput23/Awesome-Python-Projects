# Implementation of classic arcade game Pong

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

import simplegui
import random

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# initialize globals

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

ball_pos = [0, 0]
ball_vel = [0, 0]

paddle1_pos = 0
paddle2_pos = 0

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# helper function

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    
    vx = random.randrange(120, 240) // 60
    vy = -random.randrange(60, 180) // 60
    
    if direction == LEFT:
        vx = -vx 
    
    ball_vel = [vx, vy]
        
# ----------------------------------------------------------------
# ----------------------------------------------------------------

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    # initialize these global variables to their default values
    score1 = score2 = 0
    
    paddle1_pos = HEIGHT // 2 - 10
    paddle2_pos = HEIGHT // 2 - 10

    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball(bool(random.randrange(0,2)))
# ----------------------------------------------------------------
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 3, "purple")	# mid line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "red")		# gutters
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "green")
    
    # draw a circle
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], 85, 4, "Purple")

        
    
    # update ball    
    ball_pos[0] = ball_pos[0] + ball_vel[0]  
    ball_pos[1] = ball_pos[1] + ball_vel[1]        
    
    # collision with top or bottom wall (just inverse the vertical velocity]
    if (ball_pos[1] - BALL_RADIUS <= 0) or (ball_pos[1] + BALL_RADIUS >= HEIGHT):
        ball_vel[1] = -ball_vel[1]
       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 13, "Purple")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 7, "White") 
    
        
    # update paddle's vertical position, keep paddle on the screen
     
    if not (((paddle1_pos + paddle1_vel) <= 0) or ((paddle1_pos + paddle1_vel + PAD_HEIGHT) >= HEIGHT)):
        paddle1_pos = paddle1_pos + paddle1_vel 
            
    if not (((paddle2_pos + paddle2_vel) <= 0) or ((paddle2_pos + paddle2_vel + PAD_HEIGHT) >= HEIGHT)):
        paddle2_pos = paddle2_pos + paddle2_vel      
        

    # draw paddles
    canvas.draw_line([0, paddle1_pos],[0, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "white")
    canvas.draw_line([WIDTH, paddle2_pos],[WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "white")

    
    # determine whether paddle and ball collide    
    
    if (ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH:
        
        # Ball hit paddle1
        if ((ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= (paddle1_pos + PAD_HEIGHT))): 
            
            ball_vel[0] = -ball_vel[0]	
            ball_vel[0] += (ball_vel[0] // 10)
            ball_vel[1] += (ball_vel[1] // 10)
            
        else:
            score2 += 1
            spawn_ball(True)

    elif (ball_pos[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
        
        # Ball hit paddle2
        if ((ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= (paddle2_pos + PAD_HEIGHT))): 
            
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += (ball_vel[0] // 10)
            ball_vel[1] += (ball_vel[1] // 10)
            
        else:
            score1 += 1
            spawn_ball(False)
            
    # draw score
    canvas.draw_text(str(score1), [180, 50], 55, "Red") # left player score
    canvas.draw_text(str(score2), [420, 50], 55, "Lime") # right player score          
# ----------------------------------------------------------------
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # updating the velocities of paddles
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
   

# ----------------------------------------------------------------

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    # making a paddle motionless
    
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    elif (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
    
# ----------------------------------------------------------------  
# ----------------------------------------------------------------    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# ----------------------------------------------------------------
# ----------------------------------------------------------------

# start frame
new_game()
frame.start()

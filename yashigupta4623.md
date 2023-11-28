* text=auto
import turtle

emo=turtle.Turtle()

#to make center of circle --face of emoji

emo.up()
emo.goto(0,-100)
emo.down()

#fill the yellow color in the circle

emo.begin_fill()
emo.pendown()  #it is used to fill the pixel basically it trace th epoints like circle over here
emo.fillcolor('yellow') #as all emi=oji are mostly yellow so i too use yellow colour
emo.circle(100) #size of circle
emo.end_fill()

#semicircle smile in the emoji
emo.up()
emo.goto(-67,-40)
emo.setheading(-60)
emo.width(5)
emo.down()
emo.circle(80,120)
emo.fillcolor("black")  #black_color-for_smile

#to make eyes

for i in range(-35,105,70):
    emo.up()
    emo.goto(i,35)
    emo.setheading(0)
    emo.down()
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()
emo.penup() #we will pen as up so afetr it goes to end point it will affect our smiley
emo.goto(0,-150) #minus is for downward and positive is for upside --here we will send cusor to bottom 
#we will not use hide turtle because it will destroy screen as sooon as it will complete it drawing part
# to remain screen on we will use mainloop

turtle.mainloop()

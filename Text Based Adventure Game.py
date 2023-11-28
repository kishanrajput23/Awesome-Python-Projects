                                       # Python Text RPG GAme

# defining main function
def main():
    pass

if __name__ == '__main__':
    main()
from random import randint

import pygame
from pygame import mixer
pygame.init()
mixer.music.load('Everlasting Devotion.mp3')
mixer.music.play(-1)

# Creating character of the game
class Character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
  def do_damage(self, enemy):
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0: print(enemy.name +" evades "+ self.name +"'s attack.") 
    else: print(self.name+" hurts "+ enemy.name+"!") 
    return enemy.health <= 0
    
# Creating Enemy of the game
class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a goblin'
    self.health = randint(1, player.health)

# Defining attributes of the character 
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
  
  # Defining quit function
  def quit(self):    
    print(self.name+" can't find the way back home, and dies of starvation.\nR.I.P.") 
    self.health = 0
  
  # Defining help function
  def help(self): print(Commands.keys())     
  
  # Defining status function
  def status(self): print(self.name+"'s health: "+str(self.health)+"/"+str(self.health_max))
  
  # Defining tired function
  def tired(self):      
    print (self.name+" feels tired. ")
    self.health = max(1, self.health - 1)

  # Defining rest function
  def rest(self):       
    if self.state != 'normal': print (self.name+" can't rest now! "); self.enemy_attacks()
    else:
      print(self.name+" rests. ") 
      if randint(0, 1):
        self.enemy = Enemy(self)
        print(self.name+ " is rudely awakened by "+self.enemy.name+ "!")
        self.state = ' fight '
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print(self.name +" slept too much.") ; self.health = self.health - 1
  
  # Defining epxlore function
  def explore(self):         
    if self.state != 'normal':
      print(self.name+" is too busy right now!")
      self.enemy_attacks()
    else:
      print(self.name +" explores a twisty passage.")
      if randint(0, 1):
        self.enemy = Enemy(self)
        print (self.name+" encounters " +self.enemy.name+"!") 
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
 
  # Defining flee function
  def flee(self):          
    if self.state != 'fight': print(self.name+" runs in circles for a while.") ; self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print(self.name+" flees from "+self.enemy.name+".")
        self.enemy = None
        self.state = 'normal'
      else: print(self.name+" couldn't escape from "+ self.enemy.name+"!"); self.enemy_attacks()
  
  # Defining attack function
  def attack(self):        
    if self.state != 'fight': print(self.name +" swats the air, without notable results."); self.tired()
    else:
      if self.do_damage(self.enemy):
        print(self.name+ " executes "+self.enemy.name+"!")
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print (self.name+" feels stronger!" )
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print (self.name+" was slaughtered by "+self.enemy.name +"!!!\nR.I.P.")

Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }


# Taking input from the user
p = Player()
p.name = input("What is your character's name? ")
print("(type help to get a list of actions)\n")
print('''On his way back to India '''+p.name+'''experienced a disastrous plane crash. Fortunately he survived. When he came to his 
consciousness he realised that he is on a very dense jungle. He has to survive on this jungle in order to make his route to home. ''')
print(p.name+" enters a dark cave, searching for some food.")

while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print(p.name+" doesn't understand the suggestion.") 

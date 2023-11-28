# importing modules
import time
import pyautogui
#import pyautogui
 
# returns a point  object with
# x and y values
print(pyautogui.position())
 
# returns a size object with
# width and height of the screen
print(pyautogui.size())

# moves to (519,1060) in 1 sec
pyautogui.moveTo(519, 1060, duration = 1)
 
# simulates a click at the present
# mouse position
pyautogui.click()
 
# moves to (1717,352) in 1 sec
pyautogui.moveTo(1717, 352, duration = 1)
 
# simulates a click at the present
# mouse position
pyautogui.click()

# moving the cursor left 498 px & down
# 998px from it's current position
pyautogui.moveRel(-498,996, duration = 1)
 
# clicks at the present location
pyautogui.click()
 
# moves to the specified location
pyautogui.moveTo(1165,637, duration = 1)
 
# right clicks at the present cursor
# location
pyautogui.click(button="right")
 
# moves to the specified location
pyautogui.moveTo(1207,621, duration = 1)
 
# clicks at the present location
pyautogui.click()

# cursor moves to a specific position
pyautogui.moveTo(519,1060, duration = 1)
 
# left clicks at the current position
pyautogui.click()
 
# cursor moves to a specific position
pyautogui.moveTo(1550,352, duration = 1)
 
# left clicks and holds and moves the
# curson to (500,500) position
pyautogui.dragTo(500,500, duration = 1)
 
# drags the cursor relative to it's
# position to 5opx right and 50 px down
pyautogui.dragRel(50,50, duration=1)


# used to access time related functions
#import time
#import pyautogui
 
# pauses the execution of the program
# for 5 sec
time.sleep(5)
 
# types the string passed inside the
# function
pyautogui.typewrite("Github")

# pauses the execution of the program
# for 5 sec
time.sleep(5)
 
# types the string passed inside the
# function
pyautogui.typewrite("Geeks For Geeks!")
 
# simulates pressing the enter key
pyautogui.press("enter")
 
# simulates pressing the hotkey ctrl+a
pyautogui.hotkey("ctrl","a")

# a alert displays with a ok button
# on it
pyautogui.alert(text='', title='', button='OK')
 
# a confirm dialog box appears with ok
# and cancel buttons on it
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])
 
# a prompt displays that lets you to
# write something
pyautogui.prompt(text='', title='' , default='')
 
# a password field appears with entry box
# to fill a password
pyautogui.password(text='', title='', default='', mask='*')

# takes a screenshot of the present
# window and stores it as "123.png"
pyautogui.screenshot("abc.png")

# Introduction to the Temperature Converter application

The following shows the Temperature Converter application that we are going to build. The application converts a temperature from Fahrenheit to Celsius:
Basically, the application has a label, an entry, and a button. When you enter a temperature in Fahrenheit and click the Convert button, it’ll convert the value in the textbox from Fahrenheit to Celsius.
If you enter a value that cannot be converted to a number, the program will show an error.

- To build this application, we need to follow these steps.

- First, import the tkinter module, ttk submodule, and the showerror function from tkinter.messagebox:
 code:

 import tkinter as tk
 from tkinter import ttk
 from tkinter.messagebox import showerror

- Second, create the root window and set its configurations:
 code:
  # root window
  root = tk.Tk()
  root.title('Temperature Converter')
  root.geometry('300x70')
  root.resizable(False, False)

- Third, define a function that converts a temperature from Fahrenheit to Celsius:
 code:

  def fahrenheit_to_celsius(f):
     """ Convert fahrenheit to celsius
     """
     return (f - 32) * 5/9

- Fourth, create a frame that holds form fields:
code:
 frame = ttk.Frame(root)

- Fifth, define an option that will be used by all the form fields:
 code:
  options = {'padx': 5, 'pady': 5}

-Sixth, define the label, entry, and button. The label will show the result once you click the Convert button.
- Finally, place the frame on the root window and run the mainloop() method.
code:
 frame.grid(padx=10, pady=10)
 root.mainloop()

 # With this, we have successfully made our temperature convertor. 
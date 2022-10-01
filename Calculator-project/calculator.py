# calculator project

import os

# clears the screen after one calculation
clear = lambda: os.system('cls')

# function to add
def add(n1, n2):
  return n1 + n2

# function to subtract
def subtract(n1, n2):
  return n1 - n2

# function to multiply
def multiply(n1, n2):
  return n1 * n2

# function to divide
def divide(n1, n2):
  return n1 / n2

# arithemetic operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# function to calculate and display the output of the calculation
def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
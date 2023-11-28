''' This is a python begginner's program made to check whether a given string is
a palindrome or not.'''

# Function for checking the palindrome
def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    string = string.lower().replace(" ", "")
    # Check if the string is equal to its reverse by slicing
    if string == string[::-1]:
        return True
    else:
        return False

# Take the input
string = input("Enter a Word: ")
# Call the function and print the output
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")


'''

Example #1
Input - >>> Enter a Word: Racecar
Output - >>> Racecar is a palindrome.

Example #2
Input - >>> Enter a Word: Github
Output - >>> Github is not a palindrome.

'''


'''
Feel free to ask any questions
I am Akhil aka @AkhilProto
'''

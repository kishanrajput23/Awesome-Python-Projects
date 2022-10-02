import random
import string

def rand_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result)

rand_string(8)

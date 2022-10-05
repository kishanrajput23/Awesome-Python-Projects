# TODO
from cs50 import get_string

text = get_string("Text: ")

# Getting every word in text using split
# words = len((text.split()))

letters = 0
words = 0
sentences = 0

for char in text:
    if char.isalpha():
        letters += 1
    if char.isspace():
        words += 1
    if char in ['!', '.', '?']:
        sentences += 1
words += 1
print(words)
print(letters)
print(sentences)
L = (letters / words) * 100
L = round(L, 2)
S = (sentences / words) * 100
S = round(S, 2)

index = round(0.0588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

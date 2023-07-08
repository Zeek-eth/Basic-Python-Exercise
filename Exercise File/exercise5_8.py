# Import string
import string
# ask the user for a word
# ask the user for a shift number
word = input("Word:\n")
number = int(input("Number based on the word:\n"))
# for numbers greater than 26
if number > 26:
    number = number%26
# the cipher logic calculations
# Do not stress yourself just flow with it lol
alphabet = string.ascii_letters
number = alphabet[number:] + alphabet[:number]
table = str.maketrans(alphabet, number)
cipher = word.translate(table)
# print results
print(f"Cipher:{cipher}")







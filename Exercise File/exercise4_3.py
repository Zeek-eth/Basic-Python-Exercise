# text first
# print the text
text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!\n"
print(text)
# replace fox with duck
text = text.replace("fox", "duck")
print(text)
# input a word to replace
# check if the word is in the text
# replace it if the there and if not print word not found
word = input("Which word should be removed?:\n")
if word in text:
    text = text.replace(word, "")
    print(f"{text}\n")
else:
    print("Word not found\n")
# know the text lenght
# print the numbers of characters
# replace all dots with a new line
text_lenght = len(text)
print(f"{text_lenght} Characters.\n")
#for number of words in the text
space_count = 0
for character in text:
    if character == " ":
        space_count = space_count + 1
text_count = space_count + 1
print(f"Amount of words in text {text_count} words.\n")
text = text.replace(".", "\n")
print(text)
# ask user for a sentence
usertext = input("Write a sentence:\n")
user_len = len(usertext)
# Check if the statement is less than or bigger than 20
# then print the corresponding string
if user_len < 20:
    print(usertext)
elif user_len > 20:
    sub_user = usertext[0:20]
    print(f"{sub_user}...")

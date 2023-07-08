# the given fruits basket
basket = ["apple",
          "banana",
          "cherry",
          "carrot",
          "potato",
          "tomato",
          "cabbage"]
# ask user for number
word = input("Which word to ignore?\n")
# get number of fruits in basket
amount = len(basket)
# if word given is numeric
# convert word to integer
if word.isnumeric():
    word = int(word) - 1
    # interval of the int
    if 0 <= word <= 6:
        word = basket[word]
# for all fruits in basket
for fruit in range(amount):
    # If word is not in basket
    if word not in basket:
        # print this
        print("Word not found.")
        # break the loop
        break
    # if the word is on basket
    elif word == basket[fruit]:
        # Skip the word
        continue
    # And print all other fruits
    print(basket[fruit])
#Numbers to words
help_dict_1 = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}
#Words to numbers
help_dict_2 = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}

text = input("Do you want to convert numbers to words (numbers) or words to numbers (words)?\n")
# if words convert to numbers
# print number
if text == 'words':
    given_str = input("Given words (words with space):\n")
    result = ' '.join(help_dict_2[ele] for ele in given_str.split())
    print(result)
# if number converts to words
# print words
elif text == 'numbers':
    given_number = input("Given numbers (numbers in space):\n")
    result = ' '.join(help_dict_1[ele] for ele in given_number.split())
    print(result)
else:
    print("Wrong format")
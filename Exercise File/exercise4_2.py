# ask user for text
text = input("Give some text:\n")
# Invert text
# Print inverted text
rev_text = text[::-1]
print(rev_text)
# Check if they are the same
if text == rev_text:
    print("Palindrome: YES")
else:
    print("Palindrome: NO")

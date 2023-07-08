# create a list of 10 random names
random = ["houston", "john", "brooklyn", "adrian", "patrick", "dashing", "janne", "beginning", "dorian", "silvestre"]
# the new random names
new_random = []
# without s in the word
without_s = [x for x in random if 's' not in x]
# without a in the word
without_a = [x for x in without_s if 'a' not in x]
# to get the length of every word in without_a
for w in without_a:
    w_len = len(w)
    # to check if the word is less than 8
    # check the number of vowels
    # print only name that contains more than 2 vowels
    if w_len < 8:
        count = list(map(random.count, "AEIOUaeiou"))
        if sum(count) <= 2:
            pass
    else:
        new_random.append(w)
print(new_random)

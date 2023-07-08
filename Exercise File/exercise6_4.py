# the list of products
products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y82018_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]
# Ask the user for the year
# for every year picked print the codes
ask = input("Search codes for which year?\n")
# for each product
each = []
# for every goods in products
# split into codes and year
for goods in products:
    each = goods.split("_")
    # if ask for each year
    # print corresponding code
    if ask == each[1]:
        print(each[0])

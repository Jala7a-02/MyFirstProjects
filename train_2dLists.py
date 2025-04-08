fruits = ["apple", "banana" , "orange", "coconut"]
vegs = ["potato", "carrot", "calery"]
meats = ["beaf", "checken", "turkey"]

groceries = [fruits, vegs, meats]

for list in groceries :
    for item in list :
        print(item, end=" ")
    print()


#  2D calculator :

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9) , ("*", 0 , "#"))


for tuple in num_pad :

    for item in tuple :

        print (item,end= " ")

    print()
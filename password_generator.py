import random
import string

text = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
chioce = input("generate a password ? (y/n)")

while chioce == "y" :
    password = ""
    length = int(input("chose the length of the password it should be > 12 "))
    if length < 12 :
        print("length too short")
        continue
    for _ in range(length) :
        password += random.choice(text)

    print("Your password is : ",password)
    print()
    print("you can generate another password if you dont like this one")
    chioce = input("generate another password ? (y/n)")
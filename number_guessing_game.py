import random

low = 1

high = 100

number = random.randint(low, high)

guesses = 0

print("python guessing game :")
print(f"try to guess a number from {low} to {high}")

guess = int(input("try to guess the number "))

while True :

    if guess == number :

        
        break

    elif guess > number :

        print("OH NO! you guessed to high, please try again")

        guesses += 1
        
        guess = int(input("try to guess the number "))
    
    elif guess < number :

        print("OH DEAR, you guessed to low , please try again")

        guesses += 1

        guess = int(input("try to guess the number "))


print(f"CONGRATS!! , you've guessed the number after {guesses} tries")




    

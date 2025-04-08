import random

words = ("apple", "banana", "orange", "coconut", "pineapple")

# dicitionary of key():

hangman_art = {
    0 : ("   ",
         "   ", 
         "   "),
    1 : (" o ",
         "   ",
         "   "),
    2 : (" o ",
         " | ",
         "   "),
    3 : (" o ",
         " |\\ ",
         "   "),
    4 : (" o ",
         "/|\\ ",
         "   "),
    5 : (" o ",
         "/|\\",
         "/  "),
    6 : (" o ",
         "/|\\",
         "/ \\")
}

def display_man(wrong_guesses) :
    print("***************")
    for line in hangman_art[wrong_guesses] :
        print(line)
    print("***************")

def display_hint(hint) :
    print(" ".join(hint))

def display_answre(answer):
    print(" ".join(answer))

def main() :

    secret_word = random.choice(words)
    find_word = ["_"] * len(secret_word)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running :
        display_man(wrong_guesses)
        display_hint(find_word)
        choice = input("selsec a letter (a-z) :").lower()

        if len(choice) != 1 or not choice.isalpha():
            print("invalid input")
            continue

        if choice in guessed_letters :
            print(f"{choice} have been already chosen")
            continue
        guessed_letters.add(choice)

        if choice in secret_word :
            for i in range(len(secret_word)) :
                if secret_word[i] == choice :
                    find_word[i] = choice
        else :
            wrong_guesses +=1
 
        if "_" not in find_word :
            display_man(wrong_guesses)
            display_answre(secret_word)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1 :
            display_man(wrong_guesses)
            display_answre(secret_word)
            print("YOU LOSE")
            is_running = False
            

        
            
                

    



main()
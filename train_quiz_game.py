questions = ("what is my name : ?",
             "how old i am : ?", 
             "5+5 ? ", 
             "7*7 ? ",
             "speed of ligt")


options = (("mansour", "alhadi", "algozoli"), 
           ("42", "62", "23"), 
           ("12", "39", "10"),
           ("128", "49", "55"),
           ("fast", "very fast", "super ultra fast"))

answers = ("mansour",
           "23",
           "10",
           "49",
           "super ultra fast")

guesses = []

score = 0

question_num = 0


for question in questions :

    print("======================================")

    print(question)

    for option in options[question_num] :

        print(option)


    guess = input("insert the question's answer : ")

    guesses.append(guess)


    if guess == answers[question_num]:
        score+= 1
        print("CORRECT!")
    else :
        print("INCORRECT!")
        print(f"te correct answer is {answers[question_num]}")
    
    question_num += 1


print("-----------------------")
print("-------RESULT---------")
print("----------------------")

print ("answers : ", end = " ")
for answer in answers:
    print(answer,end=" ")
    
print()

print ("guesses : ", end = " ")
for guess in guesses:
    print(guess,end=" ")
print()
 
print(f"your overall score is : {score}")






     
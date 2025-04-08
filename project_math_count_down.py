import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand =12
total_problems = 10

def generate_problem() :

    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)
    expr = str(left) +" "+ operator +" "+ str(right)
    answer = eval(expr)
    return expr, answer
wrong = 0
input("press enter to start : ")
print("________________________")
start_time = time.time()

for i in range(total_problems) :
    expr , answer = generate_problem()
    while True :
        guess = input((f"problem #{i+1} : {expr} = ?"))
        if (guess) == str(answer) :        
            break
        else :
            print("try again")
            wrong +=1

solving_time = time.time() - start_time

print("________________________")
print(f"it took you {int(solving_time)} seconds to solve this problem")



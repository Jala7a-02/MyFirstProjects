def arithmetic_arranger(problems, show_answers=False):
    #check the length of the list
    if len(problems) > 5 :
        return "Error: Too many problems."
    #check operand
    valid = ["+","-"]
    operators = []
    for problem in problems :
        z = problem.split()
        operators.append(z[1])
    for operator in operators :
        if operator not in valid:
            return "Error: Operator must be '+' or '-'."
    #check if number is digit
    for problem in problems :
        z = problem.split()
        if not z[0].isdigit() or not z[2].isdigit():
            return "Error: Numbers must only contain digits."
        #check length of the number
        elif len(z[0]) > 4 or len(z[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    first_row = ""
    second_row = ""
    answers_row = ""
    dashes = ""
    #calculate answers    
    answers = []
    for problem in problems :
        answers.append(eval(problem))
        z = problem.split()
        space_width = max(len(z[0]),len(z[2])) + 2
        first_row += z[0].rjust(space_width)
        second_row += z[1] + z[2].rjust(space_width - 1)
        dashes += "-" * space_width + " "
    for i in range(len(problems)) :
        if i != len(problem) - 1 :
            first_row += " " *4
            second_row += " " *4
            answers_row += " " *4
            dashes += " " *4
    # for problem in problems :
    #     z = problem.split()
    #     space_width = space_width = max(len(z[0]),len(z[2])) + 2
    #     answers_row += str(answers[i]).rjust(space_width)
    # print(answers)
    print("\n".join((first_row,second_row,dashes)))    


    

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
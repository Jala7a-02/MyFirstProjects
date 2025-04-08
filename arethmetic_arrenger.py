def arithmetic_arranger(problems, show_answers=True):
    #check the length of the list
    if len(problems) > 5 :
        return "Error: Too many problems."
    #check operand
    valid = ["+","-"]
    operators = []
    for problem in problems :
        splitted_problem = problem.split()
        operators.append(splitted_problem[1])
    for operator in operators :
        if operator not in valid:
            return "Error: Operator must be '+' or '-'."
    #check if number is digit
    for problem in problems :
        splitted_problem = problem.split()
        if not splitted_problem[0].isdigit() or not splitted_problem[2].isdigit():
            return "Error: Numbers must only contain digits."
        #check length of the number
        elif len(splitted_problem[0]) > 4 or len(splitted_problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    first_line = ""
    second_line = ""
    dashes = ""
    answers_line = ""
    for problem in problems :
        # split the problem to get num1, operator, num2
        splitted_problem = problem.split(" ")
        # check which number is the longest to get spaces " " according to it
        lenght = len(splitted_problem[0])
        for i in range(len(splitted_problem)) :
            if len(splitted_problem[i]) > lenght :
                lenght = len(splitted_problem[i])
            else :
                continue
        # add each number to the correct line
        if len(splitted_problem[0]) > len(splitted_problem[2]):
            first_line += splitted_problem[0].rjust(lenght + 2) + "    "
            second_line += splitted_problem[1] + splitted_problem[2].rjust(lenght + 1) + "    "
        elif len(splitted_problem[0]) < len(splitted_problem[2]) or \
              len(splitted_problem[0]) == len(splitted_problem[2]):
            first_line += splitted_problem[0].rjust(lenght + 2 )+"    "
            second_line += splitted_problem[1] + splitted_problem[2].rjust(lenght + 1) + "    "
        dashes+= "-"*(lenght+2) + "    "
        answer = eval("".join(splitted_problem))
        answers_line += str(answer).rjust(lenght + 2) + "    "
    #removing the extra spaces at the end of each line
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    dashes = dashes.rstrip()
    answers_line = answers_line.rstrip()
    # merge every thing in one variable
    if show_answers :
        final_format = "\n".join((first_line,second_line,dashes,answers_line))    
    else :
        final_format = "\n".join((first_line,second_line,dashes))    



    return final_format





print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')





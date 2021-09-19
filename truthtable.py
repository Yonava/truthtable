def main():
    num = int(input('# of Vars: '))
    vars = [input(f'Name Var {x+1}: ') for x in range(num)]
    truthiness = [bool(input(f'Is {vars[x]} T or F: ')) for x in range(num)]
    print(vars)
    buildStatement(vars, truthiness)

def buildStatement(variables, tf):
    extraChars = ['&', '!', '|', '(', ')'] # operators
    statement = list(input("Tell me the equation (use &/|) along with variable names: "))
    equation = []
    for i in statement:
        if i in variables:
            storetf = variables.index(i)
            equation.append(tf[storetf])
        if i in extraChars: equation.append(i)
 
    compute(equation, statement, variables, extraChars)

def compute(set, statement, vars, operators):
    # sourcery skip: merge-nested-ifs, remove-pass-elif, remove-redundant-if
    i = 0
    # answer = []
    # while len(answer) != 1:
    #     if set[i]:
    #         if set[i+1] == '&':
    #             if set[i+2]:
    #                answer.append(True)
    #             elif not set[i+2]:
    #                 answer.append(False)
    #         elif set[i+1] == '|':
    #             answer.append(True)         

    #     elif not set[i]:
    #         if set[i+1] == '&':
    #             answer.append(False)
    #         elif set[i+1] == '|':
    #             if set[i+2]:
    #                 answer.append(True)
    #             elif not set[i+2]: 
    #                 answer.append(False)
    
    # print(*statement, '=', *answer)

    solve = []
    answer = []
    while i < len(set):
        if i == '!':
            i += 1
            if set[i]: solve.append(False)
            elif not set[i]: solve.append(True)
        elif set[i] in vars:
            if set[i]: solve.append(True)
            elif not set[i]: solve.append(False)

        if i == '&':
            i += 1
            if set[i] == '!':
                i += 1
                if solve[0] or set[0]: 
                    answer.append(False)
                    solve.remove(0)
                elif not set[i] and not set[0]:
                    answer.append(True)
                    solve.remove(0)
            elif set[i] and solve[0]: 
                    answer.append(True)
                    solve.remove(0)
            elif not set[i]:
                answer.append(False)
                solve.remove(0)



        i += 1

    print(set)
    print(answer)
if __name__ == "__main__": main()
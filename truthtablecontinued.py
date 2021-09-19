def main():
    num = int(input('# of Vars: '))
    vars = [input(f'Name Var {x+1} (only use one character): ') for x in range(num)]
    truthiness = [bool(input(f'Is {vars[x]} T or F: ')) for x in range(num)]
    print(vars)
    buildStatement(vars, truthiness)

def buildStatement(variables, tf):
    extraChars = ['&', '!', '|', '(', ')'] # operators
    statement = input("Tell me the equation (use &/|) along with variable names: ")
    equation = []
    for i in statement:
        if i in variables:
            storetf = variables.index(i)
            equation.append(tf[storetf])
        if i in extraChars: equation.append(i)
 
    parce(equation)

def parce(equation):

    print(equation)

    while '(' in equation:
        for i in range(len(equation)):
            if equation[i] == '(': x = i
            if equation[i] == ')': 
                y = i
                equation.pop(y)
                equation.pop(x)
                print(equation[x:y-1])
                sub_equation = equation[x:y-1]
                for _ in range(x,y-2):
                    equation.pop(x)
                break
        equation[x] = compute(sub_equation, True)
        print(equation)
    compute(equation, False)

def compute(set, id):
   
    i = 0

    while '!' in set:
        if set[i] == '!':
            set.pop(i)
            set[i] = not set[i]
            print(set)
        i += 1

    i = 0

    while len(set) > 1:

        if set[i] == '&':
            if set[i - 1] and set[i + 1]:
                for _ in range(2): set.pop(i-1)
                set[i-1] = True
            else:
                for _ in range(2): set.pop(i-1)
                set[i-1] = False
            i = 0
        elif set[i] == '|':
            if set[i - 1] or set[i + 1]:
                for _ in range(2): set.pop(i-1)
                set[i-1] = True
            else:
                for _ in range(2): set.pop(i-1)
                set[i-1] = False
            i = 0
        else:
            i += 1

        print(set)

    if id:
        return bool(set[0])

    print('Final Answer:',*set)
  

if __name__ == "__main__": main()
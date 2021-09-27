import time
numVars = int(input("# of Vars: "))
vars = [input(f"{v+1} Var Name: ") for v in range(numVars)]
statement = input("Tell me the equation (use &/|) along with variable names: ")
masterlist = [[] for _ in range(numVars)]

def main():
    
    powers = [2**t for t in range(1, numVars+1)]
    default = False
    for i in range(len(masterlist)):
        masterlist[i] = [x%(2**i) for x in range(powers[-1])]
        for b in range(len(masterlist[i])):
            if masterlist[i][b] == 0: default = not default
            masterlist[i][b] = default
    print(*vars, sep= ' ', end='   ')
    print(*statement, sep='')
    print('---------------')
    buildStatement(vars, statement, masterlist)

def buildStatement(variables, statement, masterlist):

    equation, extraChars = [], ['&', '!', '|', '(', ')', '=', '>'] # and, not, or, open bracket, close bracket, equality, implication  
    
    for a in statement:
        if a in variables:
            equation.append(masterlist[variables.index(a)][0])
        
        if a in extraChars:
            equation.append(a)

    for o in range(len(masterlist)): 
        if masterlist[o][0]: print('T', end= ' ')
        else: print('F', end= ' ')

    parce(equation)

def parce(equation):

    while '(' in equation:
        for i in range(len(equation)):
            if equation[i] == '(': x = i
            if equation[i] == ')': 
                y = i
                equation.pop(y)
                equation.pop(x)
                sub_equation = equation[x:y-1]
                for _ in range(x,y-2):
                    equation.pop(x)
                break
        equation[x] = compute(sub_equation, True)
    compute(equation, False)

def compute(set, id):  # sourcery no-metrics skip: assign-if-exp, boolean-if-exp-identity, hoist-statement-from-if, merge-duplicate-blocks, remove-redundant-if, split-or-ifs

    i = 0

    while '!' in set:
        if set[i] == '!':
            set.pop(i)
            set[i] = not set[i]
        i += 1

    i = 0

    while len(set) > 1:

        if set[i] == '&':
            if set[i - 1 ] and set[i + 1]:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = True
            else:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = False
            i = 0
        elif set[i] == '|':
            if set[i - 1] or set[i + 1]:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = True
            else:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = False
            i = 0
        elif set[i] == '=': 
            if set[i - 1] == set[i + 1]:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = True
            else:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = False
            i = 0
        elif set[i] == '>': 
            if set[i - 1] == set[i + 1] or set[i + 1]:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = True
            else:
                for _ in range(2): set.pop(i - 1)
                set[i - 1] = False
            i = 0
        else:
            i += 1
    

    if id:
        if set[0]: print('(T)', end= ' ')
        else: print('(F)', end= ' ')
        time.sleep(.01) # for cool effect!
        return bool(set[0])

    print('=', *set)
    if len(masterlist[0]) > 1: 
        for x in range(len(masterlist)):
            masterlist[x].pop(0)
        buildStatement(vars, statement, masterlist)

if __name__ == "__main__": main()

def CYK_checking(CNF, string_input):
    """
    javascript parsing using CYK algorithm
    """
    listString = string_input.split(" ")
    numString = len(listString)
    T = [[set([]) for j in range(numString)] for i in range(numString)]

    for j in range(numString):
        for LHS, RHS in CNF.items():
            for rule in RHS:
                if len(rule) == 1 and rule[0] == listString[j]:
                    T[j][j].add(LHS)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for rule in body:
                        if len(rule) == 2 and rule[0] in T[i][k] and rule[1] in T[k + 1][j]:
                            T[i][j].add(head)

    return len(T[0][numString - 1]) != 0


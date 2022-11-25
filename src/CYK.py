def CYK_Checking(CNF, string_input):
    W = string_input.split(" ")
    N = len(W)
    T = [[set([]) for j in range(N)] for i in range(N)]

    for j in range(N):
        for head, body in CNF.items():
            for rule in body:
                if len(rule) == 1 and rule[0] == W[j]:
                    T[j][j].add(head)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for rule in body:
                        if len(rule) == 2 and rule[0] in T[i][k] and rule[1] in T[k + 1][j]:
                            T[i][j].add(head)

    return len(T[0][N - 1]) != 0


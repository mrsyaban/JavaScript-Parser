
newStart = {"START" : [['S']]}
CFG = {**newStart, **CFG}

list_RHS = list(CFG.values())
list_LHS = list(CFG.keys())
list_Rules = list(CFG.items())

epsilonProduct = {}



for i in range(len(list_RHS)) :
    product = list_RHS[i]
    for RHS in product :
        if 'ε' in RHS :
            epsilonProduct.update({list_Rules[i][0] : list_Rules[i][1]})
            break



for i in list(epsilonProduct.items()) :
    print(i)
    print("\n")
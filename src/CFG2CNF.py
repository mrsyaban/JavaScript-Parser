def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "\n":
        head, body = baris.replace("\n", "").split(" -> ")
        body = body.split("|")

        cfg[head] = [body[0].split(" ")]

        for i in range(1, len(body)) :
            cfg[head].append(body[i].split(" "))

        baris = file.readline()

    file.close()

    return cfg

def is_terminal(string):
    list_of_terminal = [
    'pass', 'break', 'cont', 'id', 'eq', 'plus',
    'min', 'mult', 'div', 'mod', 'amp', 'bor',
    'bnot', 'gt', 'lt', 'var', 'let', 'dot',
    'case', 'default', 'continue', 'not',
    'and', 'or', 'is', 'in', 'exc', 'jgn', 'lupa',
    'tambahin', 'incremen', 'dan', 'decremen',
    'tilde', 'throw', 'str', 'int', 'xbo', 'false',
    'true', 'null', 'import', 'from', 'as',
    'wildcard', 'lc', 'rc', 'comma', 'if', 'lp', 'rp',
    'else', 'while', 'for', 'sc', 'const', 'with',
    'return', 'function', 'def', 'class', 'colon',
    'lb', 'rb', 'nl']
    
    return string in list_of_terminal

def is_variables(string):
    return not is_terminal(string)

def CFG_to_CNF(CFG):
    # STEP 1: If the start symbol S occurs on some right side, create a new start symbol S' and a new production S' -> S.
    list_head = list(CFG.keys())
    list_body = list(CFG.values())
    start_symbol = list_head[0]
    add_new_rule = False

    for rules in list_body:
        for rule in rules:
            if start_symbol in rule:
                add_new_rule = True
                break
        if add_new_rule:
            break

    if add_new_rule:
        new_rule = {"START" : [[start_symbol]]}
        new_rule.update(CFG)
        CFG = new_rule

    # STEP 2: Remove unit productions.
    contain_unit = True

    while contain_unit:
        unit_productions = {}
        contain_unit = False
        
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and is_variables(rule[0]):
                    contain_unit = True
                    if head not in unit_productions.keys():
                        unit_productions[head] = [[rule[0]]]
                    else:
                        unit_productions[head].append([rule[0]])

        for head_unit, body_unit in unit_productions.items():
            for rule_unit in body_unit:
                for head, body in CFG.items():
                    if len(rule_unit) == 1 and head == rule_unit[0]:
                        new_rule = {head_unit : body}
                        if head_unit not in CFG.keys():
                            CFG[head_unit] = body
                        else:
                            for rule in body:
                                if rule not in CFG[head_unit]:
                                    CFG[head_unit].append(rule)
    
        for head_unit, body_unit in unit_productions.items():
            for rule_unit in body_unit:
                if len(rule_unit) == 1:
                    CFG[head_unit].remove(rule_unit)

    # STEP 3: Replace Body with 3 or more Variables
    new_productions = {}
    del_productions = {}

    i = 0
    for head, body in CFG.items():
        for rule in body:
            head_symbol = head
            temp_rule = [r for r in rule]
            if len(temp_rule) > 2:
                while len(temp_rule) > 2:
                    new_symbol = f"X{i}"
                    if head_symbol not in new_productions.keys():
                        new_productions[head_symbol] = [[temp_rule[0], new_symbol]]
                    else:
                        new_productions[head_symbol].append([temp_rule[0], new_symbol])
                    head_symbol = new_symbol
                    temp_rule.remove(temp_rule[0])
                    i += 1
                else:
                    if head_symbol not in new_productions.keys():
                        new_productions[head_symbol] = [temp_rule]
                    else:
                        new_productions[head_symbol].append(temp_rule)
                    
                    if head not in del_productions.keys():
                        del_productions[head] = [rule]
                    else:
                        del_productions[head].append(rule)

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    # STEP 4: Replace Terminal adjacent to a Variables
    new_productions = {}
    del_productions = {}

    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and is_terminal(rule[0]) and is_terminal(rule[1]):
                new_symbol_Y = f"Y{j}"
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, new_symbol_Z]]
                else:
                    new_productions[head].append([new_symbol_Y, new_symbol_Z])
                    
                new_productions[new_symbol_Y] = [[rule[0]]]
                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and is_terminal(rule[0]):
                new_symbol_Y = f"Y{j}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, rule[1]]]
                else:
                    new_productions[head].append([new_symbol_Y, rule[1]])

                new_productions[new_symbol_Y] = [[rule[0]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1

            elif len(rule) == 2 and is_terminal(rule[1]):
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[rule[0], new_symbol_Z]]
                else:
                    new_productions[head].append([rule[0], new_symbol_Z])

                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                k += 1

            else:
                pass

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)

    return CFG
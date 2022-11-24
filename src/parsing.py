import re

test = open("test/inputAcc.js", "r")
teks = test.read()

symbol = [
'\\\\',
'\[',
'\]', 
'\^',
'\.',
'\|',
'\?',
'\*',
'\+',
'\{',
'\}',
'\(',
'\)',
'\;',
'\<',
'\>',
'\,',
'\"',
"\'",
'\-',
'\=',
'\=',
'\!',
'\#',
'/'
]

splitted = teks.split()

# print(splitted)
# for i in splitted :
#     print(i)

for simbol in symbol :
    result = []
    for word in splitted :
        temp = re.split(r"[A-z]*(" + simbol + r")[A-z]*", word)
        print(temp)
        for i in temp :
            if i != '' :
                result.append(i)
    # print(result)
    splitted = result


print(result)


# list = []
# # print(hasil)
# for i in hasil :
#     x = i.split()
#     for j in x :
#         list.append(j)

# print(hasil)

# for i in list :
#     for j in range(len(token)) :
#         if (token[j][0]) == i : 
#             hasil.append(token[j][1])
# print(list)
# print(" ".join(hasil))

# def, anjay, '(', ')'
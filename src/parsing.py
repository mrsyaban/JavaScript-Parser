import re
# test = open("test/inputAcc.js", "r")

# print(test.read())
teks = "def (asu) 88 8\\n"
token = [(r"\def", "DEF"), 
         (r"\(", "KBKI"),
         (r"\)", "KBKA")]


hasil = re.split(r"[A..z]*(\()[A..z]*",teks)


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
'\==',
'\=',
'\!',
'\#'
]

splitted = teks.split()

print(splitted)
# for i in splitted :
#     print(i)

for simbol in symbol :
    result = []
    for word in splitted :
        temp = re.split(r"[A..z]*(" + simbol + r")[A..z]*", word)
        for i in temp :
            if i != '' :
                result.append(i)

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
from os import pipe
import codecs

global CNF
CNF = {}


def getCNF(pathCNF):
    file = codecs.open(pathCNF, encoding="utf-8").read()
    grammarCNF = file.split('\n')
    # print(len(grammarCNF))
    lengthGrammar = len(grammarCNF)

    for rule in range (9999999):
        #melakukan split antara lhs dengan rhs dan menghapus space antar item
        try:
            lhs = grammarCNF[rule].split(' -> ')[0]
        except IndexError:
            continue
        try:
            rhs = grammarCNF[rule].split(' -> ')[1]
        except:
            continue
        rhs = rhs.replace(" ", "")
        rhs = rhs.split('|')
        lengthRHS = len(rhs)
        #iterasi setiap item di RHS dan memetakan kemunculannya ada di LHS mana
        for item in range(lengthRHS):
            value = CNF.get(rhs[item])
            #jika belum pernah muncul, maka buat key baru
            if (value == None):
                CNF.update({rhs[item]: [lhs]})
            #jika sudah pernah muncul, maka tambahkan LHS kemunculan item dari RHS
            else:
                CNF[rhs[item]].append(lhs)
    # print("Panjang Grammar: "+str(lengthGrammar))
    #print(CNF)            


def cykParser(input):
    inputLength = len(input)

    #print(inputLength)
    # inisialisasi pada tabel CYK
    table = [[[] for j in range(i)] for i in range((inputLength), 0, -1)]
    # mengisi baris awal dengan mencari apakah ada production yang cocok dengan input
    for i in range(inputLength):
        # apabila ada aturan produksi yang cocok dengan input, masukkan aturan produksi ke tabel
        try:
            table[0][i].extend(CNF[input[i]])
        except KeyError:
            continue
            # print("belum terdefinisi untuk "+input[i])

    if not inputLength and "ε" in CNF:
        return True
            
    # mengisi tabel dengan algoritma CYK
    for i in range(1, inputLength):
        for j in range(inputLength - i):
            for k in range(i):
                # mencari semua aturan produksi dari hasil produksi
                for result1 in table[i - k - 1][j]:
                    for result2 in table[k][j + i - k]:
                        try:
                            table[i][j].extend(CNF[result1 + result2])
                        except KeyError:
                            # print("tidak ditemukan untuk "+ result1+result2)
                            continue

    for x in table:
        print(x)

    if len(table[-1][-1]) != 0:
        return True
    
    return False
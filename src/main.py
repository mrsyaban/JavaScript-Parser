from CYK import *
from CFG2CNF import *
from Lexer import *



if CYK_parse(CFG_to_CNF(read_grammar("D://ITB 21//KULYAHHH//SEMESTER 3//TBFO//Tubes TBFO - JS Parser//TBFO_JSParser//src//grammar.txt")), create_token("D://ITB 21//KULYAHHH//SEMESTER 3//TBFO//Tubes TBFO - JS Parser//TBFO_JSParser//src//test.txt")):
    print("ACCEPTED")
else:
    print("SYNTAX ERROR")
from CYK import *
from CFG2CNF import *
from Lexer import *



if CYK_parse(CFG_to_CNF(read_grammar("src/Context_Free_Grammar.txt")), create_token("test/test.txt")):
    print("ACCEPTED")
else:
    print("SYNTAX ERROR")
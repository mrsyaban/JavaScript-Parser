from argparse import ArgumentParser

from CYK import *
from CFG2CNF import *
from Lexer import *

# if __name__ == "__main__":
#     argument_parser = ArgumentParser()
#     argument_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

#     args = argument_parser.parse_args()

if CYK_parse(CFG_to_CNF(read_grammar("src/Context_Free_Grammar.txt")), convert_to_tokenString("test/inputAcc.js")):
    print("ACCEPTED")
else:
    print("SYNTAX ERROR")
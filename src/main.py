from argparse import ArgumentParser

from CYK import *
from CFG2CNF import *
from Lexer import *

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("file_name", type=str, help="< JavaScript_file_name >")

    args = argument_parser.parse_args()

    CNF = CFG_to_CNF(read_grammar("src/Context_Free_Grammar.txt"))
    if CYK_checking(CNF, convert_to_tokenString(args.file_name)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")
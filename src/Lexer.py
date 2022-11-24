import sys
import re
# list token untuk syntax ke token
token_exp = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Integer and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),

    # Delimiter
    (r'\n',                     "nl"),
    (r'\(',                     "lp"), # Kurung Biasa KIri
    (r'\)',                     "rp"),
    (r'\[',                     "lb"), # Kurung Siku KIri
    (r'\]',                     "rb"),
    (r'\{',                     "lc"), # Kurung Kurawal Kiri
    (r'\}',                     "rc"),
    (r'\;',                     "sc"), 
    (r'\:',                     "colon"),

    # Operator
    (r'\*\*=',                   "mult mult eq"),
    (r'\*\*',                    "mult mult"),
    (r'\/\/=',                   "div div eq"),
    (r'\/\/',                    "div div"),
    (r'\*=',                    "mult eq"),
    (r'/=',                     "div eq"),
    (r'\+=',                    "plus eq"),
    (r'-=',                     "min eq"),
    (r'%=',                     "mod eq"),
    (r'\->',                    "ARROW"),
    (r'\+',                     "plus"),
    (r'\-',                     "min"),
    (r'\*',                     "mult"),
    (r'/',                      "div"),
    (r'%',                      "mod"),
    (r'<=',                     "lt eq"),
    (r'<',                      "lt"),
    (r'>=',                     "gt eq"),
    (r'>',                      "gt"),
    (r'!=',                     "not eq"),
    (r'\==',                    "eq eq"),
    (r'\=(?!\=)',               "eq"),

    # Keyword
    (r'\bbreak\b',              "break"),
    (r'\bconst\b',              "const"),
    (r'\bswitch\b',             "switch"),
    (r'\bcase\b',               "case"),
    (r'\bcatch\b',              "catch"),
    (r'\bcontinue\b',           "cont"),
    (r'\bdefault\b',            "default"),
    (r'\bdelete\b',             "delete"),
    (r'\bvar\b',                "var"),
    (r'\blet\b',                "let"),
    (r'\bif\b',                 "if"),
    (r'\belse\b',               "else"),
    (r'\belif\b',               "else if"),
    (r'\bfor\b',                "for"),
    (r'\bwhile\b',              "while"),
    (r'\bFalse\b',              "false"),
    (r'\btrue\b',               "true"),
    (r'\bnull\b',               "null"),
    (r'\bin\b',                 "IN"),
    (r'\bis\b',                 "IS"),
    (r'\bfunction\b',           "function"),
    (r'\btry\b',                "try"),
    (r'\bfinally\b',            "finally"),
    (r'\breturn\b',             "return"),
    (r'\bfrom\b',               "from"),
    (r'\bimport\b',             "from"),
    # (r'\braise\b',              "RAISE"),
    # (r'\bwith\b',               "WITH"),
    (r'\bas\b',                 "as"),
    (r'\bobject\b',             "LIT"),
    (r'\bint\b',                "LIT"),
    (r'\bstr\b',                "LIT"),
    (r'\bfloat\b',              "LIT"),
    (r'\bcomplex\b',            "LIT"),
    (r'\blist\b',               "LIT"),
    (r'\btuple\b',              "LIT"),
    (r'\bset\b',                "LIT"),
    (r'\,',                     "comma"),
    (r'\w+[.]\w+',              "DOTEXPR"),
    (r'\.',                     "dot"),
    (r'\\\*[(?!(\\\*))\w\W]*\\\*',       "MULTILINE"),
    # (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    # (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "id"),
]


# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, token_exp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None
        for t in token_exp:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)
    print(" ".join(tokenArray))
    return " ".join(tokenArray)

# if __name__ == "__main__":
#     create_token('test.txt')

# print(create_token("D://ITB 21//KULYAHHH//SEMESTER 3//TBFO//Tubes TBFO - JS Parser//TBFO_JSParser//src//test.txt"))
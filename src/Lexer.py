import sys
import re
# list token untuk syntax ke token
token_exp = [
    (r'[ \t]+',                 None),
    (r'#[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Integer and String
    (r'\"[^\"\n]*\"',           "str"),
    (r'\'[^\'\n]*\'',           "str"),
    (r'[\+\-]?[0-9]+\.[0-9]+',  "REAL"),
    (r'[\+\-]?[1-9][0-9]+',     "int"),
    (r'[\+\-]?[0-9]',           "int"),

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
    (r'\,',                     "comma"),

    # Operator
    (r'\*\*=',                  "poweq"),
    (r'\*\*(?!\=)',             "pow"),
    (r'\*=',                    "multeq"),
    (r'\^=',                    "xoreq"),
    (r'\&\&(?!\=)',             "and"),
    (r'\|\|(?!\=)',             "or"),
    (r'\&(?!\&)\=',             "ampeq"),
    (r'\?\?\=',                 "nullishCoalescingEq"),
    (r'\&\&\=',                 "andeq"),
    (r'\|\|\=',                 "oreq"),
    (r'\?\?(?!\=)',             "nullishCoalescing"),
    (r'/=',                     "diveq"),
    (r'\+=',                    "pluseq"),
    (r'-=',                     "mineq"),
    (r'%=',                     "modeq"),
    (r'\?(?!\?)',               "question"),
    (r'\?\.',                   "optChain"),
    (r'\+(?!\=)',               "plus"),
    (r'\+\+(?!\=)',             "inc"),
    (r'\-(?!\=)',               "min"),
    (r'\-\-(?!\=)',             "dec"),
    (r'\*(?!\=)',               "mult"),
    (r'/(?!\=)',                "div"),
    (r'%(?!\=)',                "mod"),
    (r'<=',                     "lte"),
    (r'<(?!\<)',                "lt"),
    (r'>=',                     "gte"),
    (r'>(?!\>)',                "gt"),
    (r'!=',                     "neq"),
    (r'\=(?!\=)',               "eq"),
    (r'\=\=(?!\=)',             "equal"),
    (r'\=\=\=',                 "strictEqual"),
    (r'\&(?!\&)',               "amp"),
    (r'\|(?!\|)',               "bor"),
    (r'~',                      "bnot"),
    (r'!(?!\=)',                "not"),
    (r'<<(?!\<)',               "sl"),
    (r'>>(?!\>)',               "sr"),
    (r'>>>',                    "usr"),

    # (r'\/\/',                   "floor"),
    # (r'\->',                    "ARROW"),
    # (r'\/\/=',                  "div div eq"),
    
    # Keyword
    (r'\bbreak\b',              "break"),
    (r'\bconst\b',              "const"),
    (r'\bcase\b',               "case"),
    (r'\bcatch\b',              "catch"),
    (r'\bcontinue\b',           "cont"),
    (r'\bdefault\b',            "default"),
    (r'\bdelete\b',             "delete"),
    (r'\belse\b',               "else"),
    (r'\bfalse\b',              "false"),
    (r'\bfinally\b',            "finally"),
    (r'\bfor\b',                "for"),
    (r'\bfunction\b',           "function"),
    (r'\bif\b',                 "if"),
    (r'\blet\b',                "let"),
    (r'\bnull\b',               "null"),
    (r'\breturn\b',             "return"),
    (r'\bswitch\b',             "switch"),
    (r'\bthrow\b',              "throw"),
    (r'\btry\b',                "try"),
    (r'\btrue\b',               "true"),
    (r'\bvar\b',                "var"),
    (r'\bwhile\b',              "while"),
    (r'\bin\b',                 "in"),
    (r'\bfrom\b',               "from"),
    (r'\bimport\b',             "import"),
    (r'\bas\b',                 "as"),
    (r'\w+[.]\w+',              "DOTEXPR"),
    (r'\.',                     "dot"),
    (r'\\\*[(?!(\\\*))\w\W]*\\\*',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "id"),
    # (r'\bpass\b',               "pass"),
    # (r'\bis\b',                 "IS"),
    # (r'\braise\b',              "RAISE"),
    # (r'\bwith\b',               "WITH"),
    # (r'\bobject\b',             "LIT"),
    # (r'\bint\b',                "LIT"),
    # (r'\bstr\b',                "LIT"),
    # (r'\bfloat\b',              "LIT"),
    # (r'\bcomplex\b',            "LIT"),
    # (r'\blist\b',               "LIT"),
    # (r'\btuple\b',              "LIT"),
    # (r'\bset\b',                "LIT"),
    # (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    # (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
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

print(create_token("test//test.txt"))
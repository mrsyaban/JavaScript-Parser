import sys
import re
# list token untuk syntax ke token
list_of_token = [
    # komen
    (r'[ \t]+',                 None),
    (r'\/\/[^\n]*',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\\\*[(?!(\\\*))\w\W]*\\\*',       None),

    # Integer and String
    (r'\"[^\"\n]*\"',           "str"),
    (r'\'[^\'\n]*\'',           "str"),
    (r'[\+\-]?[1-9][0-9]+',     "int"),
    (r'[\+\-]?[0-9]',           "int"),

    # Delimiter
    (r'\n',                     "nl"),
    (r'\(',                     "lp"),
    (r'\)',                     "rp"),
    (r'\[',                     "lb"),
    (r'\]',                     "rb"),
    (r'\{',                     "lc"), 
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
    (r'\bof\b',                 "of"),
    (r'\w+[.]\w+',              "DOTEXPR"),
    (r'\.',                     "dot"),
    (r'[A-Za-z\_\$][\$A-Za-z0-9\_]*', "id")
]


# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, list_of_token):
    curLine = 1 # posisi baris saat ini
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    curPos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    tokens = []
    while curPos < len(teks):
        if teks[curPos] == '\n':
            cur = 1
            curLine += 1
        match = None
        for t in list_of_token:
            pattern, tag = t
            if curLine == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, curPos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break
        if not match:
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            curPos = match.end(0)
        cur += 1

    return tokens

def convert_to_tokenString(file_path):
    file = open(file_path)
    stringFile = file.read()
    file.close()

    tokenList = lexer(stringFile,list_of_token)
    tokenString = " ".join(tokenList)

    return tokenString

print(convert_to_tokenString("D:/ITB 21/KULYAHHH/SEMESTER 3/TBFO/Tubes TBFO - JS Parser/TBFO_JSParser/test/test.js"))
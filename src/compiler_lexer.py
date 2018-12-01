import ply.lex as lex

reserved = {
    "retornar" : "RETORNAR",
    "enquanto" : "ENQUANTO",
    "caso" : "CASO",
    "senao" : "SENAO",
    "scan" : "SCAN",
    "imprimir" : "IMPRIMIR",
    "funcao" : "FUNCAO"
}

tokens = [
    'ABRE_CHAVES',
    'FECHA_CHAVES',
    'ABRE_PAREN',
    'FECHA_PAREN',
    'PONTO_VIRG',
    'VIRG',
    'ATRI',
    'ADI',
    'SUB',
    'MULT',
    'DIV',
    'NUMERO',
    'ID',
    'BIGGER',
    'LESS',
    'EQUALS',
    'DIFER'
]+ list(reserved.values())

t_ABRE_CHAVES = r'\{'
t_FECHA_CHAVES = r'\}'
t_ABRE_PAREN = r'\('
t_FECHA_PAREN = r'\)'
t_PONTO_VIRG = r'\;'

t_BIGGER= r'\>'
t_LESS = r'\<'
t_EQUALS = r'\=\='
t_DIFER = r'\!\='

t_VIRG = r'\,'
t_ATRI = r'\='
t_ADI = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

t_ignore =r' '
t_ignore_COMM = r'(\/\*.*\*\/)' 
 
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t 

def t_error(t):
    print("Illegal characeters!")
    t.lexer.skip(1)

lexer = lex.lex()

# try:
#         with open('input.arn', 'r') as myfile:
#             input_file=myfile.read().replace('\n', '')
# except EOFError:
#     raise Exception("Nao foi possivel abrir o arquivo")

# lexer.input(input_file)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
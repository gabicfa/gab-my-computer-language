from compiler_lexer import *
from compiler_eval import run
from compiler_st import SymbleTable
import ply.yacc as yacc

def p_gab(p):
    '''
    gab : programa
    '''
    main_call = ('call_func', 'main', ('listvar', None))
    p[1].append(main_call)
    p[0] = p[1]
    print(p[0])
    st = SymbleTable(None)
    (run(p[1], st))
    
def p_programa(p):
    '''
    programa : ABRE_CHAVES declaracoes FECHA_CHAVES
    '''
    p[0] = p[2]

def p_declaracoes(p):
    '''
    declaracoes : declaracoes funcao
                | declaracoes listaAfirm
                | empty
    '''
    declaracoes = []
    for i in range (1, len(p)):
        if p[i] != None:
            if type(p[i]) != list:
                declaracoes.append(p[i])
            else:
                for j in p[i]:
                    declaracoes.append(j)
    p[0] = declaracoes

def p_declaracoesSemFunc(p):
    '''
    declaracoes_sem_func : declaracoes_sem_func listaAfirm
                         | empty
    '''
    declaracaoSemFunc = []
    for i in range (1, len(p)):
        if p[i] != None:
            if type(p[i]) != list:
                declaracaoSemFunc.append(p[i])
            else:
                for j in p[i]:
                    declaracaoSemFunc.append(j)
    p[0] = declaracaoSemFunc

def p_declaroesParaFunc(p):
    '''
    declaracoes_para_func : declaracoes_para_func listaAfirmFunc
                          | empty
    '''
    declaracaoParaFunc = []
    for i in range (1, len(p)):
        if p[i] != None:
            if type(p[i]) != list:
                declaracaoParaFunc.append(p[i])
            else:
                for j in p[i]:
                    declaracaoParaFunc.append(j)
    p[0] = declaracaoParaFunc

def p_funcao(p):
    '''
    funcao : FUNCAO ID ABRE_PAREN listaVar FECHA_PAREN ABRE_CHAVES declaracoes_para_func FECHA_CHAVES
    '''
    p[0] = ('func', p[2], p[4], p[7])

def p_chama(p):
    '''
    chama : ABRE_PAREN listaVar FECHA_PAREN
    '''
    p[0] = p[2]

def p_listaVar_single(p):
    '''
    listaVar : ID
             | empty
    '''
    p[0] = ('var', p[1])

def p_listaVar_list(p):
    '''
    listaVar : ID VIRG listaVar
    '''
    p[0] = ('listvar', ('var', p[1]), p[3])

def p_listaAfirm(p):
    '''
    listaAfirm : listaAfirm afirmacao
               | empty
    '''
    listaAfirm = []
    for i in range (1, len(p)):
        if p[i] != None:
            if type(p[i]) != list:
                listaAfirm.append(p[i])
            else:
                for j in p[i]:
                    listaAfirm.append(j)
    p[0] = listaAfirm

def p_listaAfirmFun(p):
    '''
    listaAfirmFunc : listaAfirmFunc afirmacaoFunc
                   | empty
    '''
    listaAfirmFunc = []
    for i in range (1, len(p)):
        if p[i] != None:
            if type(p[i]) != list:
                listaAfirmFunc.append(p[i])
            else:
                for j in p[i]:
                    listaAfirmFunc.append(j)
    p[0] = listaAfirmFunc

def p_afirmacao(p):
    '''
    afirmacao : enquanto
              | caso
              | imprimir
    '''
    p[0] = p[1]

def p_afirmacaoFunc(p):
    '''
    afirmacaoFunc : afirmacao
                  | retornar
    '''
    p[0] = p[1]

def p_afirmacao_chama(p):
    '''
    afirmacao : ID chama PONTO_VIRG
    '''
    p[0] = ('call_func', p[1], p[2])    

def p_afirmacao_atribui(p):
    '''
    afirmacao : ID atribui PONTO_VIRG
    '''
    p[0] = ('atri', p[1], p[2])

def p_atribui(p):
    '''
    atribui : ATRI ladoDir
            | ATRI scan
    '''
    p[0] = p[2]

def p_scan(p):
    '''
    scan : SCAN ABRE_PAREN FECHA_PAREN
    '''
    p[0] = ('scan', 'SCAN')

def p_imprimir(p):
    '''
    imprimir : IMPRIMIR ABRE_PAREN ladoDir FECHA_PAREN PONTO_VIRG
    '''
    p[0] = ('imprimir', p[3])

def p_ladoDir(p):
    '''
    ladoDir : termo ADI termo
            | termo SUB termo
            | termo
    '''
    if(len(p)>2):
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_retornar(p):
    '''
    retornar : RETORNAR ABRE_PAREN ladoDir FECHA_PAREN PONTO_VIRG
    '''
    p[0] = ('retornar', p[3])

def p_termo(p):
    '''
    termo : fator
          | fator MULT fator
          | fator DIV fator 
    '''
    if(len(p)>2):
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_fator_num(p):
    '''
    fator : ADI NUMERO
          | SUB NUMERO
          | NUMERO
    '''
    if(len(p)>2):
        p[0] = (p[2], ('num', p[1]))
    else:
        p[0] = ('num', p[1])

def p_fato_id(p):
    '''
    fator : ADI ID
          | SUB ID
          | ID
    '''
    if(len(p)>2):
        p[0] = (p[2], ('var', p[1]))
    else:
        p[0] = ('var', p[1])

def p_fator_ladoDir(p):
    '''
    fator : ABRE_PAREN ladoDir FECHA_PAREN PONTO_VIRG
    '''
    p[0] = p[2]

def p_fator_chama(p):
    '''
    fator : ID chama
    '''
    p[0] = ('call_func', p[1], p[2])

def p_enquanto(p):
    '''
    enquanto : ENQUANTO expressao ABRE_CHAVES declaracoes_sem_func FECHA_CHAVES
    '''
    p[0] = ('while', p[2], p[4])

def p_caso(p):
    '''
    caso : CASO expressao ABRE_CHAVES declaracoes_sem_func FECHA_CHAVES
    '''
    print('caso')
    p[0] = ('if', p[2], p[4])
    
def p_caso_senao(p):
    '''
    caso : CASO expressao ABRE_CHAVES declaracoes_sem_func FECHA_CHAVES SENAO ABRE_CHAVES declaracoes_sem_func FECHA_CHAVES
    '''
    p[0] = ('if_else', p[2], p[4], p[8])

def p_expressao(p):
    '''
    expressao : ABRE_PAREN ID BIGGER ladoDir FECHA_PAREN
              | ABRE_PAREN ID LESS ladoDir FECHA_PAREN
              | ABRE_PAREN ID EQUALS ladoDir FECHA_PAREN
              | ABRE_PAREN ID DIFER ladoDir FECHA_PAREN
    '''
    p[0] = (p[3], ('var', p[2]), p[4])

def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    ''' 
    empty : 
    '''

parser = yacc.yacc()


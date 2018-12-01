from compiler_st import SymbleTable

funcs_st = SymbleTable(None)

def run(p, st):
    if type(p) == tuple:

        if p[0] == 'func':
            funcs_st.set(p[1], p)

        elif p[0] == 'call_func':
            func = funcs_st.get(p[1])
            new_st = SymbleTable(st)
            if(len(func[0][2])!=len(p[2])):
                raise Exception("Erro nos argumentos na chamada de funcao")
            if(p[2][1] != None):
                for v in range (1, len(p[2])):
                    value = run(p[2][v], new_st)
                    new_st.set(func[0][2][v][1], value)
                run(func[0][3], new_st)
                if(new_st.check('retornar')):
                    value = new_st.get('retornar')
                return(value[0])
            else:
                run(func[0][3], new_st)

        elif p[0] == 'atri':
            value = run(p[2], st)
            st.set(p[1], value)

        elif p[0] == 'num':
            return int(p[1])

        elif p[0] == 'var':
            value = st.get(p[1])
            return value[0]

        elif p[0] == 'retornar':
            st.parent.set('retornar', run(p[1], st))

        elif p[0] == 'imprimir':
            print(run(p[1], st))
            
        elif p[0] == 'scan':
            return int(input())

        elif p[0] == 'if':
            new_st = SymbleTable(st) 
            if(run(p[1], new_st)):
                run(p[2], new_st)

        elif p[0] == 'if_else':
            new_st = SymbleTable(st)
            if(run(p[1], new_st)):
                run(p[2], new_st)
            else:
                run(p[3], new_st)
        
        elif p[0] == 'while':
            new_st = SymbleTable(st) 
            cond =run(p[1], new_st) 
            while(cond):
                run(p[2], new_st)
                cond =run(p[1], new_st)

        elif p[0] == '+':
            return run(p[1],st)+run(p[2], st)
        elif p[0] == '*':
            return run(p[1],st)*run(p[2], st)
        elif p[0] == '-':
            return run(p[1],st)-run(p[2], st)
        elif p[0] == '/':
            return run(p[1],st)//run(p[2], st)
        elif p[0] == '==':
            return run(p[1],st)==run(p[2], st)
        elif p[0] == '!=':
            return run(p[1],st)!=run(p[2], st)
        elif p[0] == '<':
            return run(p[1],st)<run(p[2], st)
        elif p[0] == '>':
            return run(p[1], st)>run(p[2], st)
    
    elif type(p) == list:
        for n in p:
            run(n, st)
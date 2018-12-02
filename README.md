# APSLogComp

## Objetivos
  * Criar uma linguagem de programação de alta produtividade

### Preliminar:
  Crie uma lista de tópicos que você gostaria que tivesse na sua linguagem. Deve conter no mínimo:  variáveis, funções, condicionais, loops e I/O:
  
  * Linguagem com palavras reservadas em português;
  * Podendo imprimir valor de expressoes matematicas envolvendo variaveis
  * Aceitando inputs para atribuir valores a variaveis
  * Pode-se definir funcões, as chamando e as atribuindo à variaveis
  * Condicões do tipo 'if, else'
  * Contas somente com inteiros

### Atividade prática

  1. Adequar a linguagem à uma GLC e estruturá-la segundo o padrão EBNF.
  2. Utilizar as ferramentas Flex e Bison (ou semelhantes) para realizar as etapas de Análise Léxica e
  Sintática.
  3. Utilizar a LLVM (ou derivadas) para implementar a sua linguagem até a fase final de compilação.
  Não é preciso implementar um compilador novo.
  4. Criar um exemplo de testes que demonstre as características da sua Linguagem.
  5. Fazer uma apresentação de 15 minutos na data da entrega final.

### EBNF

  ```
  gab : programa

  programa
      :'{' declaracoes '}'
      ;

  declaracoes 
      : declaracoes funcao
      | declaracoes listaAfirm
      | empty
      ;

  declaracoes_sem_func 
      : declaracoes_sem_func listaAfirm
      | empty
      ;

  declaracoes_para_func 
      : declaracoes_para_func listaAfirmFunc
      | empty
      ;

  funcao
      : 'funcao' id '(' listaVar ')' '{' declaracoes_para_func '}'
      ;

  chama
      :'('listaVar')'
      ;

  listaVar   
      : id
      | id ',' listaVar
      | empty
      ;

  listaAfirm
      : listaAfirm afirmacao
      | empty
      ;

  listaAfirmFunc 
      : listaAfirmFunc afirmacaoFunc
      | empty
      ;

  afirmacaoFunc 
      : afirmacao
      | retornar
      ;

  afirmacao 
      : enquanto
      | caso
      | imprimir
      | id chama ';'
      | id atribui ';'
      ;

  atribui
      :'=' ladoDir
      |'=' scan
      ;

  scan
      :'SCAN' '(' ')' ';'
      ;

  imprimir
      :'IMPRIMIR' '(' ladoDir ')' ';'
      ;

  ladoDir
      : termo
      | termo '+' termo
      | termo '-' termo 
      ;

  retornar
      : 'RETORNAR' '(' ladoDir ')' ';'
      
  termo
      : fator
      | fator '*' fator
      | fator '/' fator 
      ;

  fator 
      :'+' inteiro
      |'-' inteiro
      |'+' id
      |'-' id
      |inteiro
      |id
      |id chama
      |'(' ladoDir ')' ';'
      ;

  enquanto
      :'ENQUANTO' expressao '{' declaracoes_sem_func '}'
      ;

  caso
      :'CASO' expressao '{' declaracoes_sem_func '}'
      |'CASO' expressao '{' declaracoes_sem_func '}' 'SENAO' '{' declaracoes_sem_func '}'
      ;

  expressao
      : '(' id '>' ladoDir ')'
      | '(' id '<' ladoDir ')'
      | '(' id '==' ladoDir ')'
      | '(' id '!=' ladoDir ')'
      ;

  inteiro
      :DIGITO+
      ;

  id
      :LETRA+
      |LETRA+ [DIGITO+]
      ;

  LETRA
      :[a-z]+
      ;

  DIGITO
      :[0-9]
      ;
  ```

### Fontes

* https://www.dabeaz.com/ply/ply.html
* https://www.youtube.com/watch?v=Hh49BXmHxX8&list=PLBOh8f9FoHHg7Ed_4yKhIbq4lIJAlonn8
* https://www.dabeaz.com/ply/PLYTalk.pdf

  

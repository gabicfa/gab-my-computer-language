# GAB - my computer language - LogComp APS

## Goal
  * Create a high-productivity programming language

### Preliminary:
  Create a list of topics you would like to have in your language. Must contain at least: variables, functions, conditionals, loops and I/O:
  
  * Language with reserved words in Portuguese;
  * Being able to print the value of mathematical expressions involving variables;
  * Accepting inputs to assign values to variables;
  * You can define functions, calling them and assigning them to variables;
  * Conditions like 'if, else';
  * Mathematical expressions with integers only;

### Activity

   1. Adapt the language to a GLC and structure it according to the EBNF standard.
   2. Use Flex and Bison (or similar) tools to perform the Lexical Analysis and
   Syntactic.
   3. Use LLVM (or derivatives) to implement your language until the final compilation phase.
   No need to implement a new compiler.
   4. Create an example of tests that demonstrate the characteristics of your language.
   5. Give a 15-minute presentation on the final delivery date.

### BNF

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

### Sources

* https://www.dabeaz.com/ply/ply.html
* https://www.youtube.com/watch?v=Hh49BXmHxX8&list=PLBOh8f9FoHHg7Ed_4yKhIbq4lIJAlonn8
* https://www.dabeaz.com/ply/PLYTalk.pdf
  
Created at 2018.2

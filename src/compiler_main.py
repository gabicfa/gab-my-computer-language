from compiler_parser import parser

if __name__ == "__main__":
    try:
        with open('exemplos/input4.gab', 'r') as myfile:
            input_file=myfile.read().replace('\n', '')
    except EOFError:
        raise Exception("Nao foi possivel abrir o arquivo")

    parser.parse(input_file)
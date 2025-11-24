import sys

from lexer import Lexer
from parser import Parser
from semantic import Semantico
from codegen import GeradorCodigo
from vm import VM


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.mc>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    with open(caminho_arquivo, "r") as f:
        codigo = f.read()

    # 1) Análise léxica
    lexer = Lexer(codigo)
    tokens = lexer.analisar()

    # 2) Análise sintática
    parser = Parser(tokens)
    arvore = parser.analisar()

    # 3) Análise semântica
    semantico = Semantico()
    semantico.validar(arvore)

    # 4) Geração de bytecode
    gerador = GeradorCodigo()
    bytecode = []
    gerador.gerar(arvore, bytecode)

    # 5) Execução pela máquina virtual
    vm = VM()
    vm.executar(bytecode)


if __name__ == "__main__":
    main()

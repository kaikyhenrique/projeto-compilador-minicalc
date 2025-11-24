class VM:
    """
    Máquina Virtual simples que executa o bytecode gerado pelo compilador MiniCalc.
    Usa uma pilha para armazenar valores temporários.
    """

    def executar(self, bytecode):
        pilha = []

        for instrucao in bytecode:
            # LOAD X → empilha o número X
            if instrucao.startswith("LOAD"):
                _, valor = instrucao.split()
                pilha.append(int(valor))

            # Operações matemáticas
            elif instrucao == "ADD":
                b = pilha.pop()
                a = pilha.pop()
                pilha.append(a + b)

            elif instrucao == "SUB":
                b = pilha.pop()
                a = pilha.pop()
                pilha.append(a - b)

            elif instrucao == "MUL":
                b = pilha.pop()
                a = pilha.pop()
                pilha.append(a * b)

            elif instrucao == "DIV":
                b = pilha.pop()
                a = pilha.pop()
                pilha.append(a // b)  # divisão inteira

            # PRINT → exibe o topo da pilha
            elif instrucao == "PRINT":
                print(pilha.pop())

            else:
                raise Exception(f"Instrução desconhecida: {instrucao}")

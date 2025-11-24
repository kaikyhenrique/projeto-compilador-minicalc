class GeradorCodigo:
    """
    Gera um bytecode simples a partir da estrutura da expressão.
    Cada nodo da árvore vira uma ou mais instruções.
    """

    def gerar(self, nodo, bytecode):
        # Número: apenas carrega o valor
        if nodo.tipo == "NUM":
            bytecode.append(f"LOAD {nodo.valor}")
            return

        # Operações binárias: gera código dos filhos e depois aplica a operação
        if nodo.tipo in ["+", "-", "*", "/"]:
            self.gerar(nodo.esquerda, bytecode)
            self.gerar(nodo.direita, bytecode)

            op_map = {
                "+": "ADD",
                "-": "SUB",
                "*": "MUL",
                "/": "DIV",
            }

            instrucao = op_map.get(nodo.tipo)
            bytecode.append(instrucao)
            return

        # Comando print: gera o valor e depois imprime
        if nodo.tipo == "PRINT":
            self.gerar(nodo.esquerda, bytecode)
            bytecode.append("PRINT")
            return

        raise Exception(f"Tipo de nodo não suportado no gerador de código: {nodo.tipo}")

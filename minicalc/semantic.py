class Semantico:
    def validar(self, nodo):
        if nodo.tipo == "NUM":
            return True

        if nodo.tipo in ["+", "-", "*", "/"]:
            self.validar(nodo.esquerda)
            self.validar(nodo.direita)
            return True

        if nodo.tipo == "PRINT":
            return self.validar(nodo.esquerda)

        raise Exception("Erro semântico")

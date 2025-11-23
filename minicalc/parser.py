from .lexer import lex

class ASTNode:
    pass

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op  # "PLUS", "MINUS", "MUL", "DIV"
        self.right = right

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        token = self.current()
        if token and token.type == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Esperado {token_type}, encontrado {token}")

    def parse(self):
        node = self.statement()
        if self.current() is not None:
            raise SyntaxError("Entrada extra apos o fim da expressao.")
        return node

    def statement(self):
        tok = self.current()
        if tok and tok.type == "PRINT":
            self.eat("PRINT")
            expr = self.expr()
            return Print(expr)
        else:
            return self.expr()

    # Gramática:
    # expr  -> term ((PLUS|MINUS) term)*
    # term  -> factor ((MUL|DIV) factor)*
    # factor -> NUM | LPAREN expr RPAREN

    def expr(self):
        node = self.term()
        while self.current() and self.current().type in ("PLUS", "MINUS"):
            op = self.current()
            self.eat(op.type)
            right = self.term()
            node = BinOp(node, op.type, right)
        return node

    def term(self):
        node = self.factor()
        while self.current() and self.current().type in ("MUL", "DIV"):
            op = self.current()
            self.eat(op.type)
            right = self.factor()
            node = BinOp(node, op.type, right)
        return node

    def factor(self):
        tok = self.current()
        if tok is None:
            raise SyntaxError("Fim inesperado da expressao")

        if tok.type == "NUM":
            self.eat("NUM")
            return Num(tok.value)
        elif tok.type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node
        else:
            raise SyntaxError(f"Token inesperado: {tok}")

def parse_code(source_code: str):
    tokens = lex(source_code)
    parser = Parser(tokens)
    return parser.parse()
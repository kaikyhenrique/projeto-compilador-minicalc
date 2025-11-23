import re

TOKEN_SPEC = [
    ("NUM",    r"\d+"),
    ("PLUS",   r"\+"),
    ("MINUS",  r"-"),
    ("MUL",    r"\*"),
    ("DIV",    r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("PRINT",  r"print"),
    ("SKIP",   r"[ \t\n]+"),
    ("MISMATCH", r"."),
]

TOKEN_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def lex(source_code: str):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, source_code):
        kind = match.lastgroup
        value = match.group()

        if kind == "NUM":
            tokens.append(Token("NUM", int(value)))
        elif kind in ("PLUS", "MINUS", "MUL", "DIV", "LPAREN", "RPAREN", "PRINT"):
            tokens.append(Token(kind, value))
        elif kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Caractere inesperado: {value}")
    return tokens
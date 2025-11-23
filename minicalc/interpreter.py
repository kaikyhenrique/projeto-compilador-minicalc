from .parser import Num, BinOp, Print, parse_code, ASTNode

def eval_expr(node: ASTNode):
    if isinstance(node, Num):
        return node.value
    if isinstance(node, BinOp):
        left = eval_expr(node.left)
        right = eval_expr(node.right)
        if node.op == "PLUS":
            return left + right
        elif node.op == "MINUS":
            return left - right
        elif node.op == "MUL":
            return left * right
        elif node.op == "DIV":
            return left / right
    raise ValueError("Nodo de expressao desconhecido")

def run(source_code: str):
    ast = parse_code(source_code)
    if isinstance(ast, Print):
        value = eval_expr(ast.expr)
        print(value)
        return value
    else:
        return eval_expr(ast)
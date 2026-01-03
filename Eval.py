import math
import operator
from Tok import TokenType
from Node import ASTNode, Number, Identifier, Special, BinaryOp, UnaryOp, Call

BINARY_OPS = {
    TokenType.PLUS: operator.add,
    TokenType.MINUS: operator.sub,
    TokenType.STAR: operator.mul,
    TokenType.SLASH: operator.truediv,
    TokenType.MODULO: operator.mod,
    TokenType.POWER: operator.pow,

    TokenType.EQ: operator.eq,
    TokenType.NE: operator.ne,
    TokenType.LT: operator.lt,
    TokenType.LE: operator.le,
    TokenType.GT: operator.gt,
    TokenType.GE: operator.ge,
}

UNARY_OPS = {
    TokenType.PLUS: lambda x: +x,
    TokenType.MINUS: lambda x: -x,
}
DEFAULT_ENV = {
    "pi": math.pi,
    "e": math.e,

    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "sqrt": math.sqrt,
    "abs": abs,
    "max": max,
    "min": min,
}
class Evaluator:
    def __init__(self, env=None):
        self.env = DEFAULT_ENV.copy()
        if env:
            self.env.update(env)
    def update(self, key,val):
        self.env[key] = val
    def eval(self, node):
        if isinstance(node, Number):
            return node.value

        if isinstance(node, Identifier):
            if node.name not in self.env:
                raise NameError(f"Undefined variable '{node.name}'")
            return self.env[node.name]

        if isinstance(node, Special):
            name = node.name[1:]  # remove backslash
            if name not in self.env:
                raise NameError(f"Undefined special '{name}'")
            return self.env[name]

        if isinstance(node, UnaryOp):
            value = self.eval(node.expr)
            return UNARY_OPS[node.op](value)

        if isinstance(node, BinaryOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            return BINARY_OPS[node.op](left, right)

        if isinstance(node, Call):
            if node.func not in self.env:
                raise NameError(f"Undefined function '{node.func}'")
            func = self.env[node.func]
            args = [self.eval(arg) for arg in node.args]
            return func(*args)

        raise TypeError(f"Unknown AST node {node}")

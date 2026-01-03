
from dataclasses import dataclass
from Tok import TokenType
@dataclass
class ASTNode:
    pass

@dataclass
class Number(ASTNode):
    value: float

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class Special(ASTNode):
    name: str

@dataclass
class UnaryOp(ASTNode):
    op: TokenType
    expr: ASTNode

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    op: TokenType
    right: ASTNode

@dataclass
class Call(ASTNode):
    func: str
    args: list

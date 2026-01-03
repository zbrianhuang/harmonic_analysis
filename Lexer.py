import re
from dataclasses import dataclass
from Tok import TokenType
from Node import ASTNode, Number, Identifier, Special, BinaryOp, UnaryOp, Call

TOKEN_SPEC = [
    ("WHITESPACE", r"[ \t\n]+"),

    ("NUMBER", r"""
        (?:\d+\.\d*|\.\d+|\d+)
        (?:[eE][+-]?\d+)?
    """),

    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("SPECIAL", r"\\[a-zA-Z_][a-zA-Z0-9_]*"),


    ("POWER", r"\*\*|\^"),
    ("EQ",    r"=="),
    ("NE",    r"!="),
    ("LE",    r"<="),
    ("GE",    r">="),

    ("PLUS",   r"\+"),
    ("MINUS",  r"-"),
    ("STAR",   r"\*"),
    ("SLASH",  r"/"),
    ("MODULO", r"%"),
    ("LT",     r"<"),
    ("GT",     r">"),
    ("ASSIGN", r"="),

    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COMMA",  r","),
    ("APOSTROPHE", r"\'"),
    # Not found
    ("MISMATCH", r"."),
]
@dataclass
class Token:
    type: TokenType
    value: str
    position: int


TOKEN_REGEX = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC),
    re.VERBOSE
)



class Lexer:

    def __init__(self, text: str):
        self.text = text

    def tokenize(self):
        tokens = []
        for match in TOKEN_REGEX.finditer(self.text):
            kind = match.lastgroup
            value = match.group()
            pos = match.start()

            if kind == "WHITESPACE":
                continue
            elif kind == "MISMATCH":
                raise SyntaxError(f"Unexpected character {value!r} at {pos}")
            else:
                tokens.append(
                    Token(TokenType[kind], value, pos)
                )

        tokens.append(Token(TokenType.EOF, "", len(self.text)))
        return tokens

from enum import Enum, auto

class TokenType(Enum):
    NUMBER      = auto()
    IDENTIFIER  = auto()
    SPECIAL     = auto()

    PLUS        = auto()   # +
    MINUS       = auto()   # -
    STAR        = auto()   # *
    SLASH       = auto()   # /
    POWER       = auto()   # ** or ^
    MODULO      = auto()    # %

    LPAREN      = auto()   # (
    RPAREN      = auto()   # )
    COMMA       = auto()   # ,
    APOSTROPHE  = auto()   # '

    ASSIGN      = auto()   # =

    EQ          = auto()   # ==
    NE          = auto()   # !=
    LT          = auto()   # <
    LE          = auto()   # <=
    GT          = auto()   # >
    GE          = auto()   # >=

    EOF         = auto()
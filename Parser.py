from Tok import TokenType
from Node import ASTNode, Number, Identifier, Special, BinaryOp, UnaryOp, Call

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def consume(self, expected=None):
        token = self.current()
        if expected and token.type != expected:
            raise SyntaxError(
                f"Expected {expected}, got {token.type} at {token.position}"
            )
        self.pos += 1
        return token

    def parse(self):
        expr = self.expression()
        self.consume(TokenType.EOF)
        return expr

    def expression(self):
        return self.comparison()

    def comparison(self):
        node = self.term()
        while self.current().type in {
            TokenType.EQ, TokenType.NE,
            TokenType.LT, TokenType.LE,
            TokenType.GT, TokenType.GE
        }:
            op = self.consume().type
            right = self.term()
            node = BinaryOp(node, op, right)
        return node

    def term(self):
        node = self.factor()
        while self.current().type in {TokenType.PLUS, TokenType.MINUS}:
            op = self.consume().type
            right = self.factor()
            node = BinaryOp(node, op, right)
        return node

    def factor(self):
        node = self.power()
        while self.current().type in {
            TokenType.STAR, TokenType.SLASH, TokenType.MODULO
        }:
            op = self.consume().type
            right = self.power()
            node = BinaryOp(node, op, right)
        return node

    def power(self):
        node = self.unary()
        if self.current().type == TokenType.POWER:
            op = self.consume().type
            right = self.power()   # right-associative
            node = BinaryOp(node, op, right)
        return node

    def unary(self):
        if self.current().type in {TokenType.PLUS, TokenType.MINUS}:
            op = self.consume().type
            return UnaryOp(op, self.unary())
        return self.primary()

    def primary(self):
        tok = self.current()

        if tok.type == TokenType.NUMBER:
            self.consume()
            return Number(float(tok.value))

        if tok.type == TokenType.IDENTIFIER:
            name = tok.value
            self.consume()

            # Function call
            if self.current().type == TokenType.LPAREN:
                self.consume(TokenType.LPAREN)
                args = []
                if self.current().type != TokenType.RPAREN:
                    args.append(self.expression())
                    while self.current().type == TokenType.COMMA:
                        self.consume()
                        args.append(self.expression())
                self.consume(TokenType.RPAREN)
                return Call(name, args)

            return Identifier(name)

        if tok.type == TokenType.SPECIAL:
            self.consume()
            return Special(tok.value)

        if tok.type == TokenType.LPAREN:
            self.consume()
            expr = self.expression()
            self.consume(TokenType.RPAREN)
            return expr

        raise SyntaxError(
            f"Unexpected token {tok.type} at {tok.position}"
        )

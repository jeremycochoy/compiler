from rply import ParserGenerator
from ast import *


def _def_rules(pg):
    @pg.production('expression : PRINT expression')
    def program(p):
        print("Get print with", p)
        return Print(p[1])

    @pg.production('expression : expression + expression')
    @pg.production('expression : expression - expression')
    @pg.production('expression : expression * expression')
    @pg.production('expression : expression / expression')
    @pg.production('expression : expression % expression')
    def expression(p):
        left = p[0]
        operator = p[1]
        right = p[2]
        if operator.gettokentype() == '+':
            return Sum(left, right)
        elif operator.gettokentype() == '-':
            return Sub(left, right)
        if operator.gettokentype() == '*':
            return Mul(left, right)
        elif operator.gettokentype() == '/':
            return Div(left, right)
        elif operator.gettokentype() == '%':
            return Mod(left, right)
        else:
            raise AssertionError(f'Unknown binary operator for: {p}')

    @pg.production('expression : INTEGER')
    def integer(p):
        return Integer(p[0].value)

    @pg.production('expression : FLOAT')
    def integer(p):
        return Float(p[0].value)

    @pg.production('expression : ( expression )')
    def integer(p):
        return p[1]

    @pg.error
    def error_handle(token):
        print("How is it possible", token)
        raise ValueError(token)


def get_parser(lexer):
    all_tokens = [r.name for r in lexer.rules]
    precedence = [
        ('left', ['DEF']),
        ('left', ['=']),
        ('left', ['[', ']', ',']),
        ('left', ['IF', 'COLON', 'ELSE', 'NEWLINE', 'WHILE']),
        ('left', ['AND', 'OR']),
        ('left', ['NOT']),
        ('left', ['==', '!=', '>=', '>', '<', '<=']),
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV']),
    ]
    pg = ParserGenerator(all_tokens, precedence)

    _def_rules(pg)

    return pg.build()

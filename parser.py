from rply import ParserGenerator
from ast import *


def _def_rules(pg):
    @pg.production('block : statement NEWLINE block')
    def block_newline(p):
        return p[2].add_expression_backward(p[0])

    @pg.production('block : statement')
    def block(p):
        return Block(p[0])

    @pg.production('statement : identifier = expression')
    def statement_assignment(p):
        return Assignment(p[0], p[2])

    @pg.production('statement : expression')
    def statement_expr(p):
        return p[0]

    @pg.production('expression : PRINT expression')
    def print_expression(p):
        return Print(p[1])

    @pg.production('expression : PASS')
    def expression_pass(p):
        return None

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
            return Add(left, right)
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
    def paren(p):
        return p[1]

    @pg.production('expression : identifier')
    def identifier_expression(p):
        return p[0]

    @pg.production('identifier : IDENTIFIER')
    def identifier(p):
        return Identifier(p[0])

    @pg.production('expression : SYMBOL')
    def symbol(p):
        return Symbol(p[0])

    @pg.error
    def error_handle(token):
        pos = token.getsourcepos()
        raise ValueError(f"Ran into a {token.gettokentype()} where it wasn't expected at "
                         f"line {pos.lineno}, column {pos.colno}, index {pos.idx}.")


def get_parser(lexer):
    all_tokens = [r.name for r in lexer.rules]
    precedence = [
        ('left', ['DEF']),
        ('right', ['=']),
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

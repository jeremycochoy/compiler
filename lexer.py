from rply import LexerGenerator


def get_lexer():
    lg = LexerGenerator()

    # Constants
    lg.add('FLOAT', '-?\d+.\d+')
    lg.add('INTEGER', '-?\d+')
    lg.add('STRING', '(""".?""")|(".?")|(\'.?\')')
    lg.add('BOOLEAN', "true(?!\w)|false(?!\w)")

    # Language keywords
    lg.add('PRINT', r'print(?!\w)')
    lg.add('PASS', r'pass(?!\w)')
    lg.add('IF', 'if(?!\w)')
    lg.add('ELSE', 'else(?!\w)')
    lg.add('AND', "and(?!\w)")
    lg.add('OR', "or(?!\w)")
    lg.add('NOT', "not(?!\w)")
    lg.add('DEF', 'def(?!\w)')
    lg.add('IMPORT', 'import(?!\w)')

    # User identifiers
    lg.add('SYMBOL', ":[a-zA-Z_][a-zA-Z0-9_]+")
    lg.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]+")

    # Operators
    lg.add('==', '==')
    lg.add('!=', '!=')
    lg.add('>=', '>=')
    lg.add('<=', '<=')
    lg.add('>', '>')
    lg.add('<', '<')
    lg.add('=', '=')
    lg.add('[', r'\[')
    lg.add(']', r'\]')
    lg.add('{', '{')
    lg.add('}', '}')
    lg.add('|', r'\|')
    lg.add(',', ',')

    lg.add('.', r'\.')
    lg.add(':', ':')
    lg.add('+', r'\+')
    lg.add('-', r'\-')
    lg.add('*', r'\*')
    lg.add('/', '/')
    lg.add('%', '%')

    # Separators
    lg.add('(', r'\(')
    lg.add(')', r'\)')

    lg.add('NEWLINE', '\n')

    # Ignore spaces
    lg.ignore('[ \t\r\f\v]+')

    return lg.build()

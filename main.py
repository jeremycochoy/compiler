import rply
from lexer import get_lexer
from parser import get_parser

text_input = """print (3 + 2) * 10.0001"""

lexer = get_lexer()
parser = get_parser(lexer)

try:
    tokens = lexer.lex(text_input)
    ast = parser.parse(tokens)
    ast.eval()
except rply.errors.LexingError as err:
    print("Exception while parsing:", err)

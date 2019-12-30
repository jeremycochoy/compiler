import rply
from lexer import get_lexer
from parser import get_parser

text_input = """variable = 15 + 3
variable = variable * 100
print variable"""

lexer = get_lexer()
parser = get_parser(lexer)

try:
    tokens = lexer.lex(text_input)
    ast = parser.parse(tokens)

    print(f"ast:\t{ast}")
    res = ast.eval()
    print(f"result:\t{res}")
except rply.errors.LexingError as err:
    print("Exception while parsing:", err)

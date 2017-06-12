from rply import ParserGenerator
import ast

pg = ParserGenerator(
    ["NUMBER", "ADD", "SUBSTRACT", "MULTIPLY", "DIVIDE", "LPAREN", "RPAREN"],
    precedence=[
        ("left", ["ADD", "SUBSTRACT"]),
        ("left", ["MULYIPLY", "DIVIDE"]),
    ],
    cache_id='newspeak'
)

@pg.production('expr : NUMBER')
def expression_number(p):
    return ast.Number(int(p[0].getstr()))

@pg.production('expr : LPAREN expr RPAREN')
def expression_parens(p):
    return p[1]

@pg.production('expr : ADD expr expr')
@pg.production('expr : SUBSTRACT expr expr')
@pg.production('expr : MULTIPLY expr expr')
@pg.production('expr : DIVIDE expr expr')
def expression_binop(p):
    left = p[1]
    right = p[2]
    if p[0].gettokentype() == 'ADD':
        return ast.Add(left, right)
    elif p[0].gettokentype() == 'SUBSTRACT':
        return ast.Substract(left, right)
    elif p[0].gettokentype() == 'MULTIPLY':
        return ast.Multiply(left, right)
    elif p[0].gettokentype() == 'DIVIDE':
        return ast.Divide(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')

parser = pg.build()
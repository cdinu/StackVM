from rply import LexerGenerator

__lg = LexerGenerator()

__lg.ignore(r"\s+")
__lg.ignore(r",")
__lg.add("LPAREN", r"\(")
__lg.add("RPAREN", r"\)")
__lg.add("ADD", r"\+")
__lg.add("SUBSTRACT", r"\-")
__lg.add("MULTIPLY", r"\*")
__lg.add("DIVIDE", r"\/")
__lg.add("NUMBER", r"\d+")

lexer = __lg.build()


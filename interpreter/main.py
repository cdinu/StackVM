from lexer import lexer
from parser import parser
from stackvm.vm import VM
from context import Context

stream = lexer.lex('* (+ 22 2) (+ 3 51)');
ast = parser.parse(stream)
ctx = Context()
ast.compile(ctx)

code = ctx.getCode()
code.append(16)

vm = VM(code, 0)
vm.run()

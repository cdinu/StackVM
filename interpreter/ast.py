import stackvm.bytecode as bytecode

class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def toStr(self):
        return str(self.value)

    def compile(self, ctx):
        ctx.emitWithParam(bytecode.ICONST, self.value)


class BinOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

    def toStr(self):
        return "({0} + {1})".format(self.left.toStr(), self.right.toStr())

    def compile(self, ctx):
        self.left.compile(ctx)
        self.right.compile(ctx)
        ctx.emit(bytecode.IADD)


class Substract(BinOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

    def toStr(self):
        return "({0} - {1})".format(self.left.toStr(), self.right.toStr())

    def compile(self, ctx):
        self.left.compile(ctx)
        self.right.compile(ctx)
        ctx.emit(bytecode.ISUB)


class Multiply(BinOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

    def toStr(self):
        return "{0} x {1}".format(self.left.toStr(), self.right.toStr())

    def compile(self, ctx):
        self.left.compile(ctx)
        self.right.compile(ctx)
        ctx.emit(bytecode.IMUL)


class Divide(BinOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

    def toStr(self):
        return "{0} / {1}".format(self.left.toStr(), self.right.toStr())


from rply.token import BaseBox


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Mod(BinaryOp):
    def eval(self):
        return self.left.eval() % self.right.eval()


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class Integer:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Float:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)


class Print:
    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        return print(self.expr.eval())

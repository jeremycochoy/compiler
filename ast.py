from rply.token import BaseBox


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.__class__.__name__} {self.right})"


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


class Assignment(BinaryOp):
    def eval(self):
        assert isinstance(self.left, Identifier)
        key = self.left.name
        value = self.right.eval()
        Identifier.global_dictionary[key] = value
        return value

    def __str__(self):
        return f"({self.left} = {self.right})"


class Integer(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

    def __str__(self):
        return f"Integer({self.value})"


class Float(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)


class Print(BaseBox):
    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        return print(self.expr.eval())


class Symbol(BaseBox):
    def __init__(self, name):
        self.name = name.value

    def eval(self):
        return str(self.name)


class Identifier(BaseBox):
    global_dictionary = {}

    def __init__(self, name):
        self.name = name.value

    def eval(self):
        try:
            return Identifier.global_dictionary[self.name]
        except KeyError:
            raise ValueError(f"Undefined identifier \"{self.name}\"")

    def __str__(self):
        return f"Identifier('{self.name}')"


class Block(BaseBox):
    def __init__(self, expression):
        self.instructions = [expression]

    def add_expression_backward(self, expression):
        self.instructions = [expression] + self.instructions
        return self

    def eval(self):
        result = None
        for i in self.instructions:
            print("\tEval:", i)
            result = i.eval()
        return result

    def __str__(self):
        content = ', '.join([str(x) for x in self.instructions])
        return f"Block([{content}])"

"""
Write methods to implement the multiply, subtract
and divide operations for integers.
Only use the add operator.
"""


class Calculator(object):

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return self.add(a, -b)

    def multiply(self, a, b):
        s = 0
        for _ in range(b):
            s = self.add(s, a)

        return s

    def divide(self, a, b):
        """
        a/b = x is same as a = xb,
        Since we already know a and b we can test x until
        x * b = a
        """
        x = product = 0
        while self.add(product, b) <= a:
            product = self.add(product, b)
            x = self.add(x, 1)

        return x


calc = Calculator()
print("1+2=%d" % calc.add(1, 2))
print("3-2=%d" % calc.subtract(3, 2))
print("3*3=%d" % calc.multiply(3, 3))
print("4/2=%d" % calc.divide(4, 2))

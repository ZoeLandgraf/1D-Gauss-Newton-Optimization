import visualization as vs


class QubicPolynomial:
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    def F(self, x):
        return self.a*(x**3) + self.b*(x**2) + self.c*x + self.d

    def f_(self, x):
        # first derivative of quadratic
        return self.a*3*(x**2) + self.b*2*x + self.c

    def ff_(self, x):
        # second derivative of the quadratic
        return self.a*3*2*x + self.b*2


import visualization as vs


class Quadratic:
    def __init__(self, a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def F(self,x):
        return self.a*x**2 + self.b*x + self.c

    def f_(self, x):
        # first derivative of quadratic
        return 2*self.a*x + self.b

    def ff_(self,x):
        # second derivative of the quadratic
        return 2*self.a


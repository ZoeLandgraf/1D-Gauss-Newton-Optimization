
class GaussNewtonOptimizer:

    def __init__(self, lr=1):
        self.lr = lr

    def optimize(self,
                 function,
                 starting_point=1,
                 nbr_it=100):
        """
            :param start_x:
            :return:
            """
        """
        Newtons optimization:
        x = a - alpha * (f'(x) / f''(x))
        """

        x = starting_point
        x_points = [starting_point] * 2
        for el in range(nbr_it):

            first_d = function.f_(x)
            second_d = function.ff_(x)

            if second_d == 0:
                raise ValueError("Second derivative is 0, here, simple Gauss Newton fails, "
                                 "please try again at a different starting point")

            temp = x - self.lr * (first_d / second_d)
            x = temp
            x_points.append(temp)

        return x_points
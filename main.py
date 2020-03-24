import numpy as np
import plotly.graph_objects as go

from QubicPolynomial import QubicPolynomial
from Quadratic import Quadratic
from _1DGaussNewtonOptimizer import GaussNewtonOptimizer
from visualization import animate_optimization



def setup(function_type,
          a = 1,
          b = 1,
          c = 1,
          d = 1,
          lr=0.1
          ):

    if function_type not in ["Polynomial", "Quadratic"]:
        raise NotImplementedError("Sorry, you can only run this with the options: 'Polynomial' or 'Quadratic' ")

    function = {"Polynomial": QubicPolynomial(a,b,c,d),
                "Quadratic": Quadratic(a,b,c)} [function_type]

    optimizer = GaussNewtonOptimizer(lr=lr)

    return function, optimizer

def optimize(
        optimizer,
        function,
        starting_point,
        nbr_it=100
             ):

    x_pos = optimizer.optimize(function, starting_point, nbr_it=nbr_it)
    return x_pos


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--function_type",
                        default="Polynomial",
                        help="")
    parser.add_argument("--starting_point",
                        default="-6",
                        type=float,
                        help="please enter a value between -5 and 5")

    parser.add_argument("--a",
                        default="-0.5",
                        type=float,
                        help="")

    parser.add_argument("--b",
                        default="6",
                        type=float,
                        help="")

    parser.add_argument("--c",
                        default="4",
                        type=float,
                        help="")

    parser.add_argument("--d",
                        default="1",
                        type=float,
                        help="")

    parser.add_argument("--nbr_it",
                        default="100",
                        type=int,
                        help="")

    parser.add_argument("--lr",
                        default="0.01",
                        type=float,
                        help="")




    args = parser.parse_args()

    if args.starting_point < -9 or args.starting_point > 9:
        raise ValueError("Please select a starting point between -9 and 9")

    function,optimizer = setup(args.function_type,
                                a=args.a,
                                b=args.b,
                                c=args.c,
                                d=args.d,
                                lr=args.lr
                                )

    x_points = optimize(optimizer,
                        function,
                        starting_point=args.starting_point,
                        nbr_it=args.nbr_it)

    animate_optimization(function, x_points)
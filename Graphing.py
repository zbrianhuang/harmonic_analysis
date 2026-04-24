import numpy as np
import matplotlib.pyplot as plt
from Lexer import Lexer
from Parser import Parser
from Eval import Evaluator


class GraphingCalculator:
    def __init__(self, expr: str, x_var="x", y_var="y",
                 iterations=100, bound=10, z_cap=None):
        self.expr = expr
        self.x_var = x_var
        self.y_var = y_var
        self.iterations = iterations
        self.bound = bound
        self.z_cap = z_cap if z_cap is not None else bound

        lexer = Lexer(expr)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        self.ast = parser.parse()

        self.evaluator = Evaluator({self.x_var: 0, self.y_var: 0})

        self.x_vals = np.linspace(-bound, bound, iterations)
        self.y_vals = np.linspace(-bound, bound, iterations)
        self.X, self.Y = np.meshgrid(self.x_vals, self.y_vals)
        self.Z = np.zeros_like(self.X)

    def evaluate_grid(self):
        for i in range(self.X.shape[0]):
            for j in range(self.X.shape[1]):
                self.evaluator.update(self.x_var, self.X[i, j])
                self.evaluator.update(self.y_var, self.Y[i, j])
                val = self.evaluator.eval(self.ast)
                # Cap Z if desired
                if abs(val) > self.z_cap:
                    val = np.sign(val) * self.z_cap
                self.Z[i, j] = val

    def plot_surface(self, title=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis')

        ax.set_xlabel(self.x_var)
        ax.set_ylabel(self.y_var)
        ax.set_zlabel("z")
        ax.set_title(title if title else f"z = {self.expr}")

        plt.show()


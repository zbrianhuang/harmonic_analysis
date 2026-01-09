from Lexer import Lexer
from Parser import Parser
from Eval import Evaluator


import numpy as np
import matplotlib.pyplot as plt
expr = ""
if 0:
    expr = "1*x**3+y**2"
else:
    expr = input("enter expr\n")

lexer = Lexer(expr)
tokens = lexer.tokenize()

parser = Parser(tokens)
ast = parser.parse()

evaluator = Evaluator({
    "x": -1,
    "y": -1,
})



ITERATIONS =200 
BOUND = 3
Z_CAP = BOUND



x_vals = np.linspace(-1*BOUND, BOUND, 2*ITERATIONS)
y_vals = np.linspace(-1*BOUND, BOUND, 2*ITERATIONS)

X, Y = np.meshgrid(x_vals, y_vals)
Z = np.zeros_like(X)
for i in range(-2*ITERATIONS,ITERATIONS):
    for j in range(-2*ITERATIONS,ITERATIONS):
        evaluator.update("x", X[i, j])
        evaluator.update("y", Y[i, j])
        a = evaluator.eval(ast)
        if abs(a)<Z_CAP:
            Z[j,i] = a
        else:
            Z[j,i] = Z_CAP
        

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("z = 4x² + 3y²")

plt.show()
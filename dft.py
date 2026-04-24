import cmath

def DFT(y):
    N = len(y)
    X = [complex(0)] * N  # initialize output

    for k in range(N):
        for n in range(N):
            X[k] += y[n] * cmath.exp(-2j * cmath.pi * k * n / N)
    return X

def IDFT(X):
    N = len(X)
    x = [complex(0)] * N

    for n in range(N):
        for k in range(N):
            x[n] += X[k] * cmath.exp(2j * cmath.pi * k * n / N)
        x[n] /= N

    return x  # keep complex; caller can take .real if desired

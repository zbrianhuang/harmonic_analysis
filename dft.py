import cmath

def dft(x):
    N = len(x)
    X = [complex(0)] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-2j * cmath.pi * k * n / N)
    return X

def idft(X):
    N = len(X)
    x = [complex(0)] * N
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * cmath.exp(2j * cmath.pi * k * n / N)
        x[n] /= N
    # The result should be real if the input was real, so we return the real part.
    # Small imaginary parts from floating point errors are discarded.
    return [val.real for val in x]

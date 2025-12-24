import numpy as np

def DFT(y):
    N = len(y)
    dft_result = np.zeros(N, dtype=np.complex128)

    for k in range(N):
        summation = 0
        for n in range(N):
            w = complex(0,1) * -2 * np.pi * k * n / N
            summation += y[n] * np.exp( w)
        dft_result[k] = summation

    return dft_result

def IDFT(Y):
    N = len(Y)
    idft_result = np.zeros(N, dtype=np.float64)

    for n in range(N):
        summation = 0
        for k in range(N):
            w = complex(0,1) * 2 * np.pi * k * n / N
            summation += Y[k] * np.exp( w)
        idft_result[n] = summation.real / N

    return idft_result
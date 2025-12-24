import numpy as np

def DFT(y):
    """
    Compute the Discrete Fourier Transform of a 1D array y.
    """
    N = len(y)
    # Create an array to store the DFT results (complex numbers)
    dft_result = np.zeros(N, dtype=np.complex128)

    # Iterate over each frequency bin k
    for k in range(N):
        # Calculate the DFT for frequency k
        summation = 0
        for n in range(N):
            w = complex(0,1) * -2 * np.pi * k * n / N
            summation += y[n] * np.exp( w)
        dft_result[k] = summation

    return dft_result

def IDFT(Y):
    N = len(Y)
    # Create an array to store the IDFT results (real numbers)
    idft_result = np.zeros(N, dtype=np.float64)

    # Iterate over each time index n
    for n in range(N):
        # Calculate the IDFT for time n
        summation = 0
        for k in range(N):
            w = complex(0,1) * 2 * np.pi * k * n / N
            summation += Y[k] * np.exp( w)
        idft_result[n] = summation.real / N

    return idft_result
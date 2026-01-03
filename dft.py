import numpy as np

def DFT(y):
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


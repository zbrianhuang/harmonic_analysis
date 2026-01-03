import cmath

def DFT(y):
    N = len(y)
    # Create an array to store the DFT results (complex numbers)
    dft_result = np.zeros(N, dtype=np.complex128)


    # Iterate over each frequency bin k
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
    
    return [val.real for val in x]

def high_pass(Y):
    total = 0
    largest = 0
    for i in Y:
        if abs(i) > largest:
            largest = abs(i)
    cutoff = 0.5*largest
    for i in range(len(Y)):
        if abs(Y[i]) < cutoff:
            Y[i] = 0
    return Y
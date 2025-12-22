import dft

import random
import math

import matplotlib.pyplot as plt
import numpy as np

def a(x): # dirac delta??
    if x>-0.02 and x<0.02: # so like 0.02 because its a discrete signal
        return 100
    else:
        return 0
def b(x): #rectangle
    if x>-0.5 and x<0.5:
        return 1
    else:
        return 0
def f(x): # noise
    return math.sin(x)+3*math.sin(10*x) +(0.2*random.random())
def g(x): # sine
    return math.sin(x)
def h(x): # yuh
    return -x**2

dist = 10
samples =dist*20
x_values = np.linspace(-1*dist, dist, samples)
y_values = np.linspace(-1*dist, dist, samples)


for i in range(len(x_values)):
    #change function here
    y_values[i] = b(x_values[i])



new_vals = dft.DFT(y_values)

sample_spacing = (x_values[-1] - x_values[0]) / (len(x_values) - 1)

N = len(y_values)
frequencies = np.fft.fftfreq(N, d=sample_spacing)

shifted_frequencies = np.fft.fftshift(frequencies)
shifted_dft = np.fft.fftshift(new_vals)


fig,axs = plt.subplots(2)
axs[0].set_title("Time Domain Signal")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Amplitude")
axs[0].plot(x_values, y_values,  color='blue')
axs[0].grid(True)


axs[1].set_title("Frequency Domain ")
axs[1].set_xlabel("Frequency in Hz")
axs[1].set_ylabel("Magnitude")
axs[1].plot(shifted_frequencies, np.abs(shifted_dft),  color='red')
axs[1].grid(True)
axs[1].set_xlim(-2, 2)


plt.tight_layout()
plt.show()






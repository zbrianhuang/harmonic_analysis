import dft
import filter

import random
import math

import matplotlib.pyplot as plt
import numpy as np

def a(x): # dirac delta??
    if x>-1 and x<1: # so like 0.02 because its a discrete signal
        return 100
    else:
        return 0
def b(x): #rectangle
    if x>-5 and x<5:
        return 1
    else:
        return 0
def f(x): # noise
    return 3*math.sin(x)+2*math.sin(4*x) +(3*random.random())
def g(x): # sine
    return math.sin(x)+ 1*random.random()
def h(x): # yuh
    return -x**2

dist = 10
samples =dist*50
x_values = np.linspace(-1*dist, dist, samples)
y_values = np.linspace(-1*dist, dist, samples)


for i in range(len(x_values)):
    #change function here
    y_values[i] =g(x_values[i])

new_vals = dft.dft(y_values)

sample_spacing = (x_values[-1] - x_values[0]) / (len(x_values) - 1)

N = len(y_values)


fig,axs = plt.subplots(3)
axs[0].set_title("Time Domain Signal")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Amplitude")
axs[0].plot(x_values, y_values,  color='blue')
axs[0].grid(True)


axs[1].set_title("Frequency Domain ")
axs[1].set_xlabel("Frequency in Hz")
axs[1].set_ylabel("Magnitude")
axs[1].plot(x_values, np.abs(new_vals),  color='red')
axs[1].grid(True)

axs[2].set_title("Reconstruction")
axs[2].set_xlabel("Time ")
axs[2].set_ylabel("")
axs[2].plot(x_values, dft.idft(filter.high_pass(new_vals)),  color='blue')
axs[2].grid(True)

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

signal = np.loadtxt('file1.txt')
x_axis = np.arange(0.005, 45.005, 0.005)

plt.plot(x_axis, signal)
plt.title("EEG signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (Micro Volts)")
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Unit Step Function
def unit_step(n):
    step = np.zeros_like(n)
    step[n >= 0] = 1
    return step

# Discrete Signal
def simulate_discrete_signal(num_samples):
    n = np.arange(-2, num_samples - 2)
    signal = unit_step(n) - unit_step(n - 3) - 5 * unit_step(n - 7)
    return n, signal

# Define the number of samples
num_samples = 14

# Simulate the signal
n, discrete_signal = simulate_discrete_signal(num_samples)

# Plot the signal
plt.figure(figsize=(10,5))
plt.stem(n, discrete_signal)

plt.title('Discrete Signal')
plt.xlabel('Sample (n)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()
import numpy as np
import matplotlib.pyplot as plt

def delta(n):
    impulse = np.zeros_like(n)
    impulse[n == 0] = 1
    return impulse

def simulate_discrete_signal(num_samples):
    n = np.arange(-3, num_samples - 3)
    signal = delta(n) + 3 * delta(n - 1) + 5 * delta(n + 1)
    return n, signal

num_samples = 7

n, discrete_signal = simulate_discrete_signal(num_samples)

plt.figure(figsize=(8,5))
plt.stem(n, discrete_signal)

plt.title('Discrete Impulse Signal')
plt.xlabel('Sample (n)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()
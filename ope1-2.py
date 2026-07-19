import numpy as np
import matplotlib.pyplot as plt

def simulate_discrete_signal(n):
    x = np.zeros(len(n))

    pattern = [2, 3, 2, 1]   # Repeating values

    for i in range(len(n)):
        x[i] = pattern[(n[i] + 3) % 4]

    return x

# Sample range
n = np.arange(-3, 7)

# Generate signal
x = simulate_discrete_signal(n)

# Plot
plt.figure(figsize=(8,4))
plt.stem(n, x)
plt.title("Discrete Periodic Signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()
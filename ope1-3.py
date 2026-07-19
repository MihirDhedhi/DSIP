import numpy as np
import matplotlib.pyplot as plt

# Continuous Piecewise Signal
def simulate_continuous_signal(time):
    signal = np.zeros_like(time)

    signal[(time >= -2) & (time < -1)] = -2
    signal[(time >= -1) & (time <= 1)] = 2 * time[(time >= -1) & (time <= 1)]
    signal[(time > 1) & (time < 2)] = 2
    signal[time >= 2] = 0

    return signal

# Define the time range
time = np.linspace(-3, 3, 1000)

# Simulate the signal
continuous_signal = simulate_continuous_signal(time)

# Plot the signal
plt.figure(figsize=(8,5))
plt.plot(time, continuous_signal, linewidth=2)

plt.title("Continuous Piecewise Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.xlim(-2, 2)
plt.ylim(-3, 3)
plt.grid(True)

plt.show()
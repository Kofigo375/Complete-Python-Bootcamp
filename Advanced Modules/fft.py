import numpy as np
import matplotlib.pyplot as plt

A = 0.5
fc = 10
phi_degrees = 30
phi_radians = np.deg2rad(phi_degrees)
fs = 32 * fc
t = np.arange(0, 2, 1/fs)
x = A * np.cos(2 * np.pi * fc * t + phi_radians)

# Compute FFT
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(X), d=1/fs)

# Extract phase
phase = np.angle(X) * 180 / np.pi

# Plot results
plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.plot(t, x)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(212)
plt.plot(freq, phase)
plt.title("Phase Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt


A0 = 1.0  # [A] at t=0
B0 = 0.0  # [B] at t=0


k_forward = 1.0  # Forward rate constant
k_reverse = 0.5  # Reverse rate constant


time = np.linspace(0, 10, 1000)
dt = time[1] - time[0]

A = np.zeros_like(time)
B = np.zeros_like(time)

A[0] = A0
B[0] = B0

for i in range(1, len(time)):
    dA = -k_forward * A[i-1] + k_reverse * B[i-1]
    dB = k_forward * A[i-1] - k_reverse * B[i-1]

    A[i] = A[i-1] + dA * dt
    B[i] = B[i-1] + dB * dt

plt.plot(time, A, label='[A]')
plt.plot(time, B, label='[B]')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Chemical Equilibrium: A ⇌ B')
plt.legend()
plt.grid(True)
plt.show()


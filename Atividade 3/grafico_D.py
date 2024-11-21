import numpy as np  # Importa a biblioteca NumPy e a apelida como np
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib (módulo pyplot) e a apelida como plt


# Adjust the range of w to vary from 0 to 40 rad/s
w = np.linspace(0, 40, 1000)  # w in rad/s, from 0 to 40
pi = np.pi
T = 7.5
# Recompute the function
Sa = np.sinc(w * pi / (T * pi))  # Sa(x) = sinc(x) in numpy
y = (2 * pi / T) * np.abs(Sa)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(w, y, label=r'$\frac{2\pi}{7.5}|\mathrm{Sa}(\frac{w\pi}{7.5})|$')
plt.xlabel('w (rad/s)')
plt.ylabel('|X(jw)|')
plt.grid(True)
plt.legend()
plt.show()

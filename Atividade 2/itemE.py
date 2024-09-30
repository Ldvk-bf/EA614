import cmath as cm

import numpy as np
from matplotlib import pyplot as plt

# Definir parâmetros
T = 7
t = np.linspace(-100, 100, 1000)  # Vetor de tempo

def H_jw(omega):
    R = 100 * 10**3
    C = 1 * 10**-6
    omega_c = 1 / (R * C)
    

    return 1 / (1 - 1j * (omega_c / omega))

H_jw_values = [np.abs(H_jw(omega)) for omega in t]
H_jw_angle_values = [np.angle(H_jw(omega)) for omega in t]

# Plotar os coeficientes
plt.stem(t, H_jw_values, linefmt='none', markerfmt='bo', basefmt='none')
plt.stem(t, H_jw_angle_values, linefmt='none', markerfmt='ro', basefmt='none')
plt.xlabel('k')
plt.ylabel('|H(jw)|')
plt.title('Coeficientes H(jw)')
plt.grid(True)
plt.show()

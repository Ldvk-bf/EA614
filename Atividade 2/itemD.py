import numpy as np
from matplotlib import pyplot as plt

# Definir parâmetros
T = 7
omega_0 = 2 * np.pi / T  # Período do sinal

def a_k(k, omega_0):
    if k == 0:
        return 0
    else:
        return (2 / (k * omega_0 * 7 * 1j)) * (
            -1
            + np.cos(k * omega_0)
            - np.cos(2 * k * omega_0)
            + np.sin(k * omega_0) / (k * omega_0)
        )
        
# Calcular os 50 primeiros coeficientes a_k
k_values = np.arange(1, 51)
a_k_values = [a_k(k, omega_0) for k in k_values]

# Plotar os coeficientes
plt.stem(k_values, np.abs(a_k_values))
plt.xlabel('k')
plt.ylabel('|a_k|')
plt.title('Coeficientes a_k')
plt.grid(True)
plt.show()
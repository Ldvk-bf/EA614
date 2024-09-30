import cmath as cm

import matplotlib.pyplot as plt
import numpy as np

# Definir parâmetros
T = 7
t = np.linspace(-3.5, 3.5, 1000)  # Vetor de tempo
# t = np.linspace(-100, 100, 1000)  # Vetor de tempo


# Definir a função a_k
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


def func_f():
    R = 10**5
    C = 10 ** (-6)
    wc = 1 / (R * C)

    vals = 1200
    w0 = (2 * np.pi) / 7
    soma = np.linspace(-3.5, 3.5, vals)
    n = 50
    lista = [0 for i in range(vals)]
    coefs = [a_k(k, w0) for k in range(-n, n + 1)]
    h = [1 / (1 - 1j * (wc / (k * w0))) if k != 0 else 0 for k in range(-n, n + 1)]
    for t in range(vals):
        for k in range(-n, n + 1):
            lista[t] += coefs[k + n] * cm.exp(1j * k * w0 * soma[t]) * h[k + n]

    plt.scatter(soma, lista, color="r")
    plt.ylabel("y(t)")
    plt.xlabel("t (s)")
    plt.show()


func_f()

import matplotlib.pyplot as plt
import numpy as np

# Definir parâmetros
T = 7
omega_0 = 2 * np.pi / T  # Período do sinal
t = np.linspace(-3.5, 3.5, 1000)  # Vetor de tempo


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


# Definir a função da série de Fourier truncada
def fourier_series_approx(N, t, omega_0):
    x_N = np.zeros_like(t, dtype=complex)
    for k in range(-N, N + 1):
        x_N += a_k(k, omega_0) * np.exp(1j * k * omega_0 * t)
    return x_N


# Função original x(t) (exemplo, ajustar conforme o problema)
def x_t(t):
    return np.piecewise(
        t,
        [
            t < -2,
            (t > -2) & (t < -1),
            (t >= -1) & (t < 0),
            (t >= 0) & (t < 1),
            (t >= 1) & (t < 2),
            t >= 2,
        ],
        [0, -1, lambda t: t + 1, lambda t: t - 1, 1, 0],
    )


# Plotar a função original e as aproximações da série de Fourier
N_values = [1, 10, 20, 50]

for i, N in enumerate(N_values):
    s = 0
    for t_i in t:
        s += (x_t(t_i) - fourier_series_approx(N, t_i, omega_0)) ** 2
    s = s / 7
    print(f"Erro quadratico medio para N={1}: {s}")

# plt.figure(figsize=(12, 10))

# Gráfico da função original
plt.subplot(2, 2, 1)
plt.plot(t, x_t(t), label="x(t)", color="black")
plt.title("Função Original x(t)")
plt.grid(True)

# Gráficos da série de Fourier truncada para diferentes valores de N
for i, N in enumerate(N_values):
    plt.subplot(2, 2, i + 1)  # Mudando para i + 2 ao invés de i + 1
    plt.plot(t, x_t(t), label="x(t)", color="black")
    plt.plot(
        t, fourier_series_approx(N, t, omega_0), label=f"Fourier N={N}", color="red"
    )
    plt.title(f"Aproximação Fourier N={N}")
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Definir as constantes
wc = 10  # Frequência de corte (rad/s)
epsilon_chebyshev = 0.6  # Parâmetro de ripple para o filtro de Chebyshev
n_chebyshev = 4  # Ordem do filtro de Chebyshev
n_butterworth = 2  # Ordem do filtro de Butterworth

# Frequências angulares (w)
w = np.linspace(0, 40, 1000)

# Definir o espectro de entrada X(jw) (exemplo: uma gaussiana centrada em 20 rad/s)
X = np.exp(-0.1 * (w - 20)**2)  # Exemplo de espectro de entrada

# 1. Filtro Passa-Baixas Ideal
H_ideal = np.where(w <= wc, 1, 0)
Y_ideal = H_ideal * X  # Saída do filtro ideal

# 2. Filtro de Chebyshev Tipo I (cálculo correto)
# Ajustar o cálculo do Polinômio de Chebyshev Tn para todas as frequências
def chebyshev_response(w, wc, n, epsilon):
    w_normalized = w / wc
    # Para |w/wc| <= 1 usamos o polinômio de Chebyshev
    Tn = np.where(w_normalized <= 1, np.cos(n * np.arccos(w_normalized)), np.cosh(n * np.arccosh(w_normalized)))
    # Fórmula do filtro de Chebyshev Tipo I
    return 1 / np.sqrt(1 + epsilon**2 * Tn**2)

H_chebyshev = chebyshev_response(w, wc, n_chebyshev, epsilon_chebyshev)
Y_chebyshev = H_chebyshev * X  # Saída do filtro de Chebyshev

# 3. Filtro de Butterworth
H_butterworth = 1 / np.sqrt(1 + (w / wc)**(2 * n_butterworth))
Y_butterworth = H_butterworth * X  # Saída do filtro Butterworth

# Plotar os módulos dos espectros de saída
plt.figure(figsize=(10, 7))
plt.plot(w, np.abs(Y_ideal), label=r'$|Y_{\text{ideal}}(j\omega)|$', linestyle='--', color='blue')
plt.plot(w, np.abs(Y_chebyshev), label=r'$|Y_{\text{Chebyshev}}(j\omega)|$', color='orange')
plt.plot(w, np.abs(Y_butterworth), label=r'$|Y_{\text{Butterworth}}(j\omega)|$', color='green')

# Configurações do gráfico
plt.title('Módulo do espectro observado na saída dos filtros')
plt.xlabel(r'Frequência angular $\omega$ (rad/s)')
plt.ylabel(r'$|Y(j\omega)|$')
plt.grid(True)
plt.legend()
plt.xlim([0, 40])
plt.show()
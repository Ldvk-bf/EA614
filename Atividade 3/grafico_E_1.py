import numpy as np
import matplotlib.pyplot as plt

# Definir as constantes
wc = 10  # Frequência de corte (rad/s)
epsilon_chebyshev = 0.6  # Parâmetro de ripple para o filtro de Chebyshev
n_chebyshev = 4  # Ordem do filtro de Chebyshev
n_butterworth = 2  # Ordem do filtro de Butterworth

# Frequências angulares (w)
w = np.linspace(0, 40, 1000)

# 1. Filtro Passa-Baixas Ideal
H_ideal = np.where(w <= wc, 1, 0)

# 2. Filtro de Chebyshev Tipo I
# Usar o polinômio de Chebyshev de ordem n
Tn_chebyshev = np.cos(n_chebyshev * np.arccos(w / wc))  # Polinômio de Chebyshev de primeira espécie
H_chebyshev = 1 / np.sqrt(1 + epsilon_chebyshev**2 * Tn_chebyshev**2)

# 3. Filtro de Butterworth
H_butterworth = 1 / np.sqrt(1 + (w / wc)**(2 * n_butterworth))

# Plotar os resultados
plt.figure(figsize=(10, 7))
plt.plot(w, H_ideal, label=r'FPB ideal', linestyle='--', color='blue')
plt.plot(w, H_chebyshev, label=r'Chebyshev', color='orange')
plt.plot(w, H_butterworth, label=r'Butterworth', color='green')

# Configurações do gráfico
plt.title('Módulo da resposta em frequência dos filtros')
plt.xlabel(r'Frequência angular $\omega$ (rad/s)')
plt.ylabel(r'Módulo $|H(j\omega)|$')
plt.grid(True)
plt.legend()
plt.xlim([0, 40])
plt.ylim([0, 1.1])
plt.show()

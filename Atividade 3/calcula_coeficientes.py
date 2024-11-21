""" Funções auxiliares para a resolução do exercício """

""" Rotina que calcula os coeficientes do polinômio de Chebyshev de maneira não-recursiva 

Parâmetros: w - vetor de frequências (sugestão: usar um vetor com amostras de 0 a 20 rad/s)
            wc - freq. de corte do filtro (em rad/s)
            n - ordem do filtro de Chebyshev
Saída:      Tn - vetor com os coeficientes calculados do polinômio de Chebyshev (possui o mesmo tamanho que w)

"""

import matplotlib.pyplot as plt
import numpy as np

w = np.linspace(0, 20, 1000)

def calcula_coeficientes(w, wc, n):

    Tn = np.zeros((w.size,))
    # determina os valores dos coeficientes segundo as expressões padronizadas
    Tn[abs(w) < wc] = np.cos(n * np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n * np.arccosh(w[abs(w) >= wc] / wc))
    return Tn

def calcula_coeficientes_Butterworth(w, wc, n):

    Tn = np.zeros((w.size,))
    # determina os valores dos coeficientes segundo as expressões padronizadas
    Tn[abs(w) < wc] = np.cos(n * np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n * np.arccosh(w[abs(w) >= wc] / wc))
    return Tn


def questao_a(w, wc, n):

    habs = np.zeros_like(w)
    habs = 1 / (1 + (w/wc) ** (2 * n))
    return habs

color = ['r', 'g', 'b', 'y', 'c']
e_param = [0.1, 0.3, 0.5, 0.7, 0.9]

for i in range(1,6):
    habs = questao_a(w, 10, i)
    
    plt.plot(w, habs, color[i], label=f'n={i}')
    plt.legend()

    
plt.show()
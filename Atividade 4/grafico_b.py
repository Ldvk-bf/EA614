import math

import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav


def espectro(y):
    Y = np.abs(np.fft.fft(y))
    w = np.linspace(0, 2 * math.pi, Y.size)

    plt.figure()
    plt.plot(w, Y)
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xlim((0, 2 * math.pi))
    plt.title('Espectro do Sinal')
    plt.show()

    return Y, w

Fs, y = wav.read('creed_overcome.wav')

y_mono = (y[:, 0] + y[:, 1]) / 2

M = 6
# Pega tudo com um passo de M
y_dec = y_mono[::M]
Fs_dec = Fs // M

espectro(y_dec)
ipd.Audio(data=y_mono, rate=Fs)



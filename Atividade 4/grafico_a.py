import math

import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio


def espectro(y):

    #modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    #frequencias avaliadas
    w = np.linspace(0,2*math.pi,Y.size)

    #exibe o grafico do espectro
    plt.figure() 
    plt.plot(w,Y)
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xlim((0,2*math.pi))
    plt.show()
    
    return Y,w  

Fs, y = sio.wavfile.read("creed_overcome.wav")
# Conversão para mono
y_mono=(y[:,0]+y[:,1])/2

ipd.Audio(y_mono, rate=Fs)
espectro(y_mono)
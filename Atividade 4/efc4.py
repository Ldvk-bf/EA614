import math

import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as iow


def kaiser(wp,wr):

    wc = (wp + wr)/2
    d = 0.01
    Ap = 20*math.log10((1+d)/(1-d))
    Ar = -20*math.log10(d)


    if Ar < 21:
        b = 0
        D = .9222

    elif Ar < 50:
        b = 0.5842*(Ar-21)**0.4+0.07886*(Ar-21)
        D = (Ar - 7.95)/14.36
    else:
        b = .1102*(Ar-8.7)
        D = (Ar - 7.95)/14.36

    k = math.ceil(math.pi*D/(wr-wp)-.5)
    M = 2*k+1

    n = np.arange(-k,k+1,1)
    
    w = np.i0(b*np.sqrt(1-(4/M**2)*n**2))
    w = np.divide(w,np.i0(b))

    h = wc/math.pi*np.sinc(wc*n/math.pi)*w

    return h


""" Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """
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


def itemA(y):
    espectro(y)


def itemB(y):
    y = [y[i] for i in range(0, len(y), 6)]
    espectro(y)


def itemC(y, Fs):
    ipd.Audio(y, rate=Fs)
    y_dec = [y[i] for i in range(0, len(y), 6)]
    ipd.Audio(y_dec, rate=Fs//6)


def itemD():
    P = [0.45, 0.45, 1.5]
    R = [2, 0.5, 2]
    for i in range(3):
        h = kaiser(P[i], R[i]) 
        espectro(h)


def itemE(y, Fs):
    P = 0.45
    R = 0.5
    h = kaiser(P, R) 
    Y = np.convolve(y,h)
    espectro(Y)
    ipd.Audio(Y, rate=Fs)


def itemF(y, Fs):
    P = 0.45
    R = 0.5
    h = kaiser(P, R) 
    Y = np.convolve(y,h)
    Y_dec = [Y[i] for i in range(0, len(Y), 6)]
    espectro(Y_dec)
    ipd.Audio(Y_dec, rate=Fs//6)


def itemG(vals):
    Y = np.abs(np.fft.fft(vals))
    w = np.linspace(0,250,Y.size)

    #exibe o grafico do espectro
    lista = [Y[i] for i in range(np.shape(Y)[0]//2)]
    k = lista.index(max(lista))
    freq = (k/Y.size) * 250
    print("fe:", freq, "Hz")

    plt.figure() 
    plt.plot(w,Y)
    plt.xlabel('$f$ [Hz]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xlim((0,125))
    plt.show()



""" Parte relativa a amostragem """
Fs, y = iow.read('creed_overcome.wav')
y=(y[:,0]+y[:,1])/2

itemA(y)
itemB(y)
itemC(y, Fs)
itemD()
itemE(y, Fs)
itemF(y, Fs)


""" Parte relativa à DFT """
fil = open('EEG.txt')
vals = np.asarray([float(x) for x in fil.read().split()])
fil.close()
itemG(vals)
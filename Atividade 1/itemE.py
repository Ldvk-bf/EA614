# x[n] = s[n] + 0.7s[n-1] - 0.04s[n-2]
# h[n] = delta[n] + 0.7delta[n-1] - 0.04delta[n-2]
# w1 = [1, -0.7, 0.7**2, -0.7**3, 0.7**4, -0.7**5, 0.7**6]
# w2 = [1, -0.2, 0.4, 0.9, -0.3, -0.9, 0.8]

import matplotlib.pyplot as plt
import numpy as np

w1 = [1, -0.7, 0.7**2, -(0.7**3), 0.7**4, -(0.7**5), 0.7**6]
w2 = [1, -0.2, 0.4, 0.9, -0.3, -0.9, 0.8]
h = [1, 0.7, -0.04]

alphabet = np.array([1+1j,1-1j,-1+1j,-1-1j])
s = np.random.choice(alphabet,(500,))

x = np.convolve(s, h)

eta=0.02*np.random.randn(x.size,)+0.02*1j*np.random.randn(x.size,)
r=x+eta

y1 = np.convolve(w1, r)
y2 = np.convolve(w2, r)

# plt.scatter(x=np.real(y1), y=np.imag(y1), color='red', label='y1[n]')
plt.scatter(x=np.real(y2), y=np.imag(y2), color='red', label='y2[n]')
plt.scatter(x=np.real(s), y=np.imag(s), color='blue', label='s[n]')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.title('Plot of s[n] and y2[n]')
plt.show()
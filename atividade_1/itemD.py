# x[n] = s[n] + 0.7s[n-1] - 0.04s[n-2]
# h[n] = delta[n] + 0.7delta[n-1] - 0.04delta[n-2]

import matplotlib.pyplot as plt
import numpy as np

h = [1, 0.7, -0.04]

alphabet = np.array([1+1j,1-1j,-1+1j,-1-1j])
s = np.random.choice(alphabet,(500,))

x = np.convolve(s, h)

# plt.scatter(x=np.real(s), y=np.imag(s), color='blue', label='s')
plt.scatter(x=np.real(s), y=np.imag(s), color='green', label='s[n]')
plt.scatter(x=np.real(x), y=np.imag(x), color='red', label='x[n]')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.legend()
plt.title('Plot of s[n] and x[n]')
plt.show()

# x[n] = s[n] + 0.7s[n-1] - 0.04s[n-2]
# h[n] = delta[n] + 0.7delta[n-1] - 0.04delta[n-2]
# w1 = [1, -0.7, 0.7**2, -0.7**3, 0.7**4, -0.7**5, 0.7**6]
# w2 = [1, -0.2, 0.4, 0.9, -0.3, -0.9, 0.8]

import numpy as np

w1 = [1, -0.7, 0.7**2, -(0.7**3), 0.7**4, -(0.7**5), 0.7**6]
w2 = [1, -0.2, 0.4, 0.9, -0.3, -0.9, 0.8]
h = [1, 0.7, -0.04]

print()
print(f"Saída equalizada com w1: {[round(num, 8) for num in np.convolve(w1, h)]}")
print(f"Saída equalizada com w2: {np.convolve(w2, h)}")

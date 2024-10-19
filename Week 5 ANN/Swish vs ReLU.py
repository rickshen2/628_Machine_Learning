import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.1,dtype= float)

silu = x / (1 + np.exp(-x))

plt.plot(x, silu)
plt.show()
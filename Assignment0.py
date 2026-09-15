#task 4
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3*np.pi, 100)

y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid(True)
plt.show()
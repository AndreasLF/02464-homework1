import matplotlib.pyplot as plt
import numpy as np

li = __import__("1_lateral_inhibiton")

w = 0.1
I = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]

A = li.activation_level(I,w)
print(A)

x = np.arange(1,len(I)-1)
plt.plot(I)
plt.plot(x,A)
plt.legend(["Input fra fotoreceptor","Aktiveringsniveau"])
plt.show()

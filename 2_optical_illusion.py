import matplotlib.pyplot as plt

li = __import__("1_lateral_inhibiton")

w = 0.1
I = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]

A = li.activation_level(I,w)
plt.plot(A)
plt.plot(I)
plt.legend(["A","I"])
plt.show()

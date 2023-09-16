import matplotlib.pyplot as plot
import math

n = int(input())
if n < 20:
    n = 20

x = []
y = []

for k in range(n):
    x.append(k * 16 * math.pi / n)
    y.append(0.1 * k * math.sin(x[k]))

plot.plot(x, y)
plot.show()

import numpy as np
import matplotlib.pyplot as plt

#f(x) = 10*sin(x) + x**2, dérivée f(x) = 10*cos(x) + 2*x
def function(x):
    return 10*np.sin(x) + x**2

def derivee(x):
    return 10*np.cos(x) + 2*x

x = np.linspace(-6,6,1000)
x_current = 6
#taux d'appr
lr = 0.01
#max_iteration
max_iteration = 100
for i in range(max_iteration):
    plt.plot(x, function(x))
    plt.scatter(x_current, function(x_current), color ='red', s = 100)
    x_current = x_current  - lr*derivee(x_current)
    plt.pause(0.001)
    plt.clf()
    
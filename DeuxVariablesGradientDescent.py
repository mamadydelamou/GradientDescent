import numpy as np
import matplotlib.pyplot as plt
# f(x,y) = x**2 + y**2 -20*sin(x), dérivée 
def function(x, y):
    return x**2 + y**2 -20*np.sin(x)
def gradient(x, y):
    return 2*x -20*np.cos(x), 2*y

X = np.linspace(-6,6,1000)
Y = np.linspace(-6,6,1000)
x,y = np.meshgrid(X,Y)
ax = plt.axes(projection = "3d", computed_zorder = False)
x_current, y_current = 0,2
lr = 0.001
max_iteration = 100
for i in range(max_iteration):
    ax.plot_surface(x,y,function(x,y))
    ax.scatter(x_current,y_current, function(x_current,y_current), color = 'blue', s = 100, zorder = 1)
    gradx, grady = gradient(x_current, y_current)
    x_current = x_current - lr*gradx
    y_current = y_current - lr*grady
    plt.pause(0.001)
    ax.clear()
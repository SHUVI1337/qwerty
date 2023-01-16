```python
Создать график функции
```


```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(-150, 100))
line, = ax.plot([], [], lw=3)
def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = 10*x**2 * np.sin(x**2 + 5)
    line.set_data(x, y)
    return line,
anim = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=200,
    interval=20,
    blit=True)
anim.save('sine_wave.gif', writer='imagemagick')
```


```python
In: f(x) = 10x^2 * sin(x^2 + 5) While x [0,5]
Out:
```

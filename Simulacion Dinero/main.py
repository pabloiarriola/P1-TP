import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

cantidad_gente = 50

n = cantidad_gente - 1
p = 1 / (cantidad_gente - 1)
dinero_inicio = 50

banco = dinero_inicio*np.ones([cantidad_gente])

range = np.arange(cantidad_gente)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

bar = plt.bar(range,banco)

def init():
    return bar

def animate(i):
    global banco, ax
    gente_sdinero = sum(banco==0)
    muestra_sdinero = np.random.binomial(cantidad_gente - 1 - gente_sdinero, p, cantidad_gente)
    muestra_codinero = np.random.binomial(cantidad_gente - gente_sdinero, p, cantidad_gente)
    muestra_sdinero[banco == 0] = 0
    muestra_codinero[banco > 0] = 0
    sample = muestra_sdinero + muestra_codinero
    banco = banco + sample - 1*(banco > 0)
    banco = np.sort(banco)
    for rect, y in zip(bar, banco):
        rect.set_height(y)
    ax.set_ylim(0,max(banco))
    ax.set_title(i)
    #print(sum(banco)/cantidad_gente)
    return bar

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=3000, interval=1, blit=False)

anim.save('animacion.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

plt.show()

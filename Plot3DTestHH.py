import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

pts = np.array([[random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,15)] for _ in range(50)])
attractors_positions = np.array(((5.0,6.0,2.0),(5.0,8.0,8.0)))

def update_graph(frame):
    global attractors_positions, data_set, stars, windows
    cos = [random.randint(0,15) for _ in range(50)]
    shp = (2,3)
    attractors_positions += np.random.rand(*shp)*2-1

    stars._offsets3d = (attractors_positions[:,0],attractors_positions[:,1],attractors_positions[:,2])

    return [data_set, stars, windows]

if __name__ == "__main__":
    cos = [random.randint(0, 15) for _ in range(50)]
    data_set = ax.scatter(xs=pts[:, 0], ys=pts[:, 1], zs=pts[:, 2], marker="o", c=cos, cmap="Set1")
    stars = ax.scatter(xs=attractors_positions[:, 0], ys=attractors_positions[:, 1], zs=attractors_positions[:, 2],
                       marker="*", c=(0, 1), cmap="Set1", s=150)
    windows = ax.scatter(xs=attractors_positions[:, 0], ys=attractors_positions[:, 1], zs=attractors_positions[:, 2],
                         marker="o", color=(1.0, 1.0, 0.0, 0.5), s=450)

    ani = animation.FuncAnimation(fig, update_graph, interval = 1000)#, blit= True, cache_frame_data=False)
    plt.show()
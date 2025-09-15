from typing import Optional, Callable, List, Tuple

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.figure import Figure


class DataVisualizer3d:
    def __init__(self):
        self.callback_function: Optional[Callable] = None

        self.fig: Figure = plt.figure()
        self.ax: Axes = self.fig.add_subplot(projection="3d")

        self.data_points: List[Tuple[int, int, int, int]] = []  # (x, y, z, color_index)
        self.data_set_plotted:Optional[PathCollection] = None

        self.attractors: List[Tuple[int, int, int]] = [] # (x, y, z)
        self.windows_plotted:Optional[PathCollection] = None
        self.stars_plotted:Optional[PathCollection] = None



    def setup_attractor_collections(self):
        attractors_np = np.array(self.attractors)
        attractor_color_indices = np.array([i for i in range(len(self.attractors))])
        self.windows_plotted = self.ax.scatter(xs=attractors_np[:, 0],
                                               ys=attractors_np[:, 1],
                                               zs=attractors_np[:, 2],
                                               marker="o",
                                               color=(1.0, 1.0, 0.0, 0.33),
                                               s=450)
        self.stars_plotted = self.ax.scatter(xs=attractors_np[:, 0],
                                             ys=attractors_np[:, 1],
                                             zs=attractors_np[:, 2],
                                             marker="*",
                                             color=attractor_color_indices,
                                             s=150)

    def setup_data_collection(self):
        data_np = np.array(self.data_points)
        self.data_set_plotted = self.ax.scatter(xs=data_np[:, 0],
                                                ys=data_np[:, 1],
                                                zs=data_np[:, 2],
                                                marker="o",
                                                c=data_np[:, 3],
                                                cmap="Set1")

    def set_looping_function(self, func:Optional[Callable]):
        self.callback_function = func

    def add_data_point(self, position: Tuple[int, int, int]|List[int], color_index:int = 0):
        new_datum:List[int] = list(position)
        new_datum.append(color_index)
        self.data_points.append(tuple(new_datum))
        self.setup_data_collection()

    def update_data_point_at_index_to_color(self, idx:int, color_index:int):
        if -1 < idx < len(self.data_points):
            self.data_points[idx][3] = color_index

    def add_attractor(self, position:List[int]|Tuple[int, int, int]):
        self.attractors.append(tuple(position))
        self.setup_attractor_collections()

    def set_attractor_position(self, attractor_index, new_position:List[int]|Tuple[int, int, int, int]):
        if -1 < attractor_index < len(self.attractors):
            self.attractors[attractor_index] = tuple(new_position)
            self.setup_attractor_collections()

    def remove_attractor_at_index(self, attractor_index):
        if -1 < attractor_index < len(self.attractors):
            del(self.attractors[attractor_index])
            self.setup_attractor_collections()

    def update_plot(self, frame):
        if self.callback_function is not None:
            self.callback_function()

        items_to_return:List[PathCollection] = []
        if len(self.data_points) > 0:
            items_to_return.append(self.data_set_plotted)
        if len(self.attractors) > 0:
            items_to_return.append(self.windows_plotted)
            items_to_return.append(self.stars_plotted)
        return items_to_return

    def start_animation(self):
        self.count = 0
        ani = animation.FuncAnimation(self.fig, func=self.update_plot, interval= 1000)
        plt.show()

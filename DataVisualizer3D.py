from typing import Optional, Callable, List, Tuple

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.figure import Figure

STAR_SIZE = 150
WINDOW_SIZE = 450


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

        self.count = 0

    def set_axis_labels(self, x_label:str, y_label:str, z_label:str):
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_zlabel(z_label)

    def setup_attractor_collections(self):
        """
        This creates the non-empty collection of windows and attractors (large circles and stars).
        Precondition: self.window_collection has length > 0.
        :return: None
        """
        attractors_np = np.array(self.attractors)
        attractor_color_indices = np.array([i for i in range(len(self.attractors))])
        self.windows_plotted = self.ax.scatter(xs=attractors_np[:, 0],
                                               ys=attractors_np[:, 1],
                                               zs=attractors_np[:, 2],
                                               marker="o",
                                               color=(1.0, 1.0, 0.0, 0.33),
                                               s=WINDOW_SIZE)
        self.stars_plotted = self.ax.scatter(xs=attractors_np[:, 0],
                                             ys=attractors_np[:, 1],
                                             zs=attractors_np[:, 2],
                                             marker="*",
                                             c=attractor_color_indices,
                                             s=STAR_SIZE)

    def setup_data_collection(self):
        """
        This creates the non-empty collection of data points (small circles).
        Precondition: self.window_collection has length > 0.
        :return: None
        """
        data_np = np.array(self.data_points)
        self.data_set_plotted = self.ax.scatter(xs=data_np[:, 0],
                                                ys=data_np[:, 1],
                                                zs=data_np[:, 2],
                                                marker="o",
                                                c=data_np[:, 3],
                                                cmap="Set1")

    def set_looping_function(self, func:Optional[Callable]) -> None:
        """
        Sets which method, if any, should be called whenever the graph is about to update.
        :param func: the method to call, or None
        :return: None
        """
        self.callback_function = func

    def add_data_point(self, position: Tuple[int, int, int]|List[int], color_index:int = 0):
        """
        add a dot on the graph at the given coordinates and the color that is at color_index in the color list. If
        color_index == -1 or is larger than the list length, adds a new color to the list and uses that.
        :param position: The (x, y) location on the graph. (0,0) is at top left
        :param color_index: the index of the color in color list to use
        :return: None
        """
        new_datum:List[int] = list(position)
        new_datum.append(color_index)
        self.data_points.append(tuple(new_datum))
        self.setup_data_collection()

    def update_data_point_at_index_to_color(self, idx:int, color_index:int):
        """
        Changes data point number idx to have the color in the color list found at color_index. If color_index is
        -1 or out of bounds of color_list, creates a new color and sets the color to that.
        :param idx: index of which data point to alter
        :param color_index: the index of the color to use.
        :return: None
        """
        if -1 < idx < len(self.data_points):
            datum = list(self.data_points[idx])
            datum[3] = color_index
            self.data_points[idx] = tuple(datum)

    def add_attractor(self, position:List[int]|Tuple[int, int, int]):
        """
        Adds an attractor to the screen at the given location with the color found in color_list at the given
        color_index. If color_index is -1 or out of bounds of color list, appends a new color to color_list and uses
        that.
        :param position: the coordinates of the attractor, (x, y). Point (0,0) is in the top left corner.
        :return: None
        """
        self.attractors.append(tuple(position))
        self.setup_attractor_collections()

    def set_attractor_position(self, attractor_index, new_position:List[int]|Tuple[int, int, int, int]):
        """
        alters the position of the attractor at the given index to a new (x, y) value
        :param attractor_index: the index of the attractor in the list
        :param new_position: the new location for this attractor.
        :return: None
        """
        if -1 < attractor_index < len(self.attractors):
            self.attractors[attractor_index] = tuple(new_position)
            self.setup_attractor_collections()

    def remove_attractor_at_index(self, attractor_index):
        """
        deletes one of the attractors from the list to draw.
        :param attractor_index: the index of the attractor to remove
        :return: None
        """
        if -1 < attractor_index < len(self.attractors):
            del(self.attractors[attractor_index])
        if len(self.attractors) > 0:
            self.setup_attractor_collections()
        else:
            self.windows_plotted = None
            self.stars_plotted = None

    def update_plot(self, frame):
        """
        This method is called automatically to animate the graph, and it calls a method set by set_looping_function.
        :param frame: Not used.
        :return: the list of collections that should be drawn. These have to be non-empty.
        """
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

        ani = animation.FuncAnimation(self.fig, func=self.update_plot, interval= 1000)
        plt.show()

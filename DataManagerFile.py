from DataVisualizer3D import DataVisualizer3d

class DataManager:
    def __init__(self):
        self.dv3 = DataVisualizer3d()
        self.dv3.set_axis_labels(x_label="X - axis title",
                                 y_label= "Y - axis title",
                                 z_label="Z - axis title")

        #  TODO: here is where you would load up your data and send the info to the datavisualizer3d. An example of
        #        data points being added is shown below. (Feel free to delete these examples when you are adding yours.)

        self.dv3.add_data_point(position=(100, 100, 50), color_index= 0)
        self.dv3.add_data_point(position=(200, 100, 150), color_index=1)
        self.dv3.add_data_point(position=(200, 200, 75), color_index=0)
        self.dv3.add_data_point(position=(30, 30, 200), color_index=-1)

        # note: this is how you'll be changing the color of a data point.
        self.dv3.update_data_point_at_index_to_color(idx=0, color_index=2)

        # TODO: here is where you should add the attractors that you wish to display (if any). These attractors have
        #       windows aroudn them, with a radius set in DataVisualizer3d.


        self.dv3.add_attractor(position=(300, 100, 150))
        self.dv3.add_attractor(position=(40, 300, 300))

        self.iteration_counter = 0

    def start(self):
        # Tell the visualizer what method should be called each time it is about to update the graph.
        self.dv3.set_looping_function(self.iterate_loop)

        # Tell the visualizer to begin animating.
        ani = self.dv3.start_animation()

    def iterate_loop(self):
        """
        This method gets called over and over again by the animation loop.
        :return:
        """
        print(self.iteration_counter)
        self.iteration_counter += 1

        # TODO: here is where you will execute a step of your algorithm.

if __name__ == "__main__":
    manager = DataManager()
    manager.start()
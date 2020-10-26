from manimlib.imports import *
import numpy as np#crude graph
class Scene1(GraphScene):
    CONFIG = {
    "x_min": -PI,
    "x_max": PI,
    "x_tick_frequency": 2*PI,
    "x_labelled_nums": [-3,2,1,0,1,2,3],
    "y_min": -1,
    "y_max": 3,
    "graph_origin": DOWN*2,
    "unit_size": 0.5
    }

    def construct(self):
        self.setup_axes(animate = True)
        labels = self.get_number_mobjects()
        self.play(ShowCreation(labels))
        func_graph1 = self.get_graph(smooth, YELLOW_E) #HAS TO BE AFTER SETUP of AXES
        func_graph2 = self.get_graph(self.mygraph, RED_C)
        self.play(ShowCreation(func_graph1), ShowCreation(func_graph2))
        self.wait(2)

    def mygraph(self,x):
        if abs(x) <= PI:
            return 1 + 4/3*np.cos(x) + 2/3*np.cos(2*x)
        else:
            return 0
    def mygraph2(self,x):
        return 1 + 4/3*np.cos(x) + 2/3*np.cos(2*x)
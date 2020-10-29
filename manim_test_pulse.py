from manimlib.imports import *
import numpy as np
class Graphing(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 8,
        "y_min": -1,
        "y_max": 2,
        "function_color": WHITE,
        "axes_color": BLUE
    }
    def func_to_graph(self,x):
    	if x<=3:
    		return 1.0
    	elif x>5:
    		return 0.3
    	else:
    	    return 0.0
        #return np.piecewise(x, [x<3, x>=5], [1, 0.3])

    def construct(self):
        test1=TextMobject("Group 7-8 Test")
        #test2=TextMobject("$$f(x)=\\sin(x)$$")
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph)
        graph_lab = self.get_graph_label(func_graph, label = "f(x)")

        self.play(Write(test1))
        self.play(FadeOut(test1))
        self.wait(1)
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(2)

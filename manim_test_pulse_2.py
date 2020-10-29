from manimlib.imports import *

class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class CustomGraph3(GraphFromData):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_label": "$\\Omega$",
        "x_tick_frequency": 10,
        "y_min": -1,
        "y_max": 2,
        "y_axis_label": "$H_{BS}$",
        "y_tick_frequency": 3,
        "function_color": WHITE,
        "axes_color": BLUE
    }
    def construct(self):
        self.setup_axes()

        # make two list
        x_ticks = [0,5,7,10]
        x_labels = ["$0^{+}$","$\\Omega_{p1}$","$\\Omega_{s1}$","$\\Omega_{0}^{-}$"]
        y_ticks = [0.2,1,1.2]
        y_labels = ["$\\delta_{2}$","$1$","$1 + \\delta_{1}$"]
        # generates VGroup with date_text positioning on their place
        def get_text_1(s,n):
            t = TextMobject(s, stroke_width=0, size=0.8)
            t.next_to(self.x_axis.n2p(n), DOWN, buff=0.2)
            return t
        def get_text_2(s,n):
            t = TextMobject(s, stroke_width=0, size=0.8)
            t.next_to(self.y_axis.n2p(n), LEFT, buff=0.2)
            return t
        x_texts = VGroup(*[get_text_1(x_label,x_tick) for x_label,x_tick in zip(x_labels,x_ticks)])
        y_texts = VGroup(*[get_text_2(y_label,y_tick) for y_label,y_tick in zip(y_labels,y_ticks)])
        self.x_axis.add(x_texts)
        self.y_axis.add(y_texts)

        x_1 = [0 , 5, 5, 7,  7,  10]
        y_1 = [1 , 1, 0, 0, 0.2, 0.2]
        x_2 = [0 , 5, 5, 7,  7,  10]
        y_2 = [1.2 , 1.2, 0, 0, 0.2, 0.2]

        coords_1 = [[px,py] for px,py in zip(x_1,y_1)]
        coords_2 = [[qx,qy] for qx,qy in zip(x_2,y_2)]
        # |
        # V
        points_1 = self.get_points_from_coords(coords_1)
        points_2 = self.get_points_from_coords(coords_2)
        
        graph_1 = DiscreteGraphFromSetPoints(points_1,color=GREEN)
        graph_2 = DiscreteGraphFromSetPoints(points_2,color=GREEN)
        #dots = self.get_dots_from_coords(coords)

        #self.add(graph)
        self.play(ShowCreation(graph_1,run_time=4),ShowCreation(graph_2,run_time=4))
        self.wait(3)

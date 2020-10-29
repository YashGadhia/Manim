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
        "x_min": -2,
        "x_max": 8,
        "y_min": -1,
        "y_max": 2,
        "function_color": WHITE,
        "axes_color": BLUE
    }
    def construct(self):
        self.setup_axes()

        # make two list
        nums = [3,5]
        dates = ['a', 'b']
        # generates VGroup with date_text positioning on their place
        def get_text(s,n):
            t = Text(s, stroke_width=0, size=0.2)
            t.next_to(self.x_axis.n2p(n), DOWN, buff=0.2)
            return t
        date_texts = VGroup(*[get_text(date,num) for date,num in zip(dates,nums)])
        self.x_axis.add(date_texts)

        x = [-2 , 3, 3, 5,  5,  8]
        y = [1 , 1, 0, 0, 0.3, 0.3]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(coords)
        
        graph = DiscreteGraphFromSetPoints(points,color=GREEN)
        dots = self.get_dots_from_coords(coords)

        #self.add(graph)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)

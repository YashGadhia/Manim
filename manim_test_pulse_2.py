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
        self.setup_axes(animate=True)

        # make two list
        x_ticks_1 = [0,5,7,10]
        x_labels_1 = ["$0^{+}$","$\\Omega_{p1}$","$\\Omega_{S1}$","$\\Omega_{0}^{-}$"]
        x_ticks_2 = [0,3,5,10]
        x_labels_2 = ["$0^{+}$","$+1$","$\\Omega_{SL1}$","$+\\infty$"]
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
        x_texts_1 = VGroup(*[get_text_1(x_label,x_tick) for x_label,x_tick in zip(x_labels_1,x_ticks_1)])
        x_texts_2 = VGroup(*[get_text_1(x_label,x_tick) for x_label,x_tick in zip(x_labels_2,x_ticks_2)])
        y_texts = VGroup(*[get_text_2(y_label,y_tick) for y_label,y_tick in zip(y_labels,y_ticks)])
        self.x_axis.add(x_texts_1)
        self.y_axis.add(y_texts)

        x_1 = [0 , 5, 5, 7,  7,  10]
        y_1 = [1 , 1, 0, 0, 0.2, 0.2]
        x_2 = [0 , 5, 5, 7,  7,  10]
        y_2 = [1.2 , 1.2, 0, 0, 0.2, 0.2]
        x_3 = [0 , 3, 3, 5, 5, 10]

        coords_1 = [[px,py] for px,py in zip(x_1,y_1)]
        coords_2 = [[qx,qy] for qx,qy in zip(x_2,y_2)]
        coords_3 = [[px,py] for px,py in zip(x_3,y_1)]
        coords_4 = [[px,py] for px,py in zip(x_3,y_2)]
        # |
        # V
        points_1 = self.get_points_from_coords(coords_1)
        points_2 = self.get_points_from_coords(coords_2)
        points_3 = self.get_points_from_coords(coords_3)
        points_4 = self.get_points_from_coords(coords_4)

        graph_1 = DiscreteGraphFromSetPoints(points_1,color=GREEN)
        graph_2 = DiscreteGraphFromSetPoints(points_2,color=GREEN)
        graph_3 = DiscreteGraphFromSetPoints(points_3,color=GREEN)
        graph_4 = DiscreteGraphFromSetPoints(points_4,color=GREEN)
        #dots = self.get_dots_from_coords(coords)

        #number_line_1 = NumberLine(x_min=0,x_max=10,color="BLUE",include_ticks=False)
        #number_line_1.add(x_texts)
        text_1 = TextMobject("Axis Transformation")

        #self.add(graph)
        self.play(ShowCreation(graph_1,run_time=4),ShowCreation(graph_2,run_time=4))
        self.wait(3)
        self.play(FadeOut(graph_1),FadeOut(graph_2))
        self.play(Write(text_1,run_time=1))
        self.play(FadeOut(self.y_axis),FadeOut(self.x_axis))
        #self.y_axis_label_mob = y_label
        #self.setup_axes(animate=True)
        #self.x_axis_label.add("$\\Omega_{L}$")
        #self.y_axis_label.add("$H_{LP}$")
        #self.x_axis.add(x_texts_2)
        #self.x_axis.add(y_texts)
        def add_x_axis(self):
            x_num_range = float(self.x_max - self.x_min)
            self.space_unit_to_x = self.x_axis_width / x_num_range
            if self.x_labeled_nums is None:
                self.x_labeled_nums = []
            if self.x_leftmost_tick is None:
                self.x_leftmost_tick = self.x_min
            x_axis = NumberLine(
                x_min=self.x_min,
                x_max=self.x_max,
                unit_size=self.space_unit_to_x,
                tick_frequency=self.x_tick_frequency,
                leftmost_tick=self.x_leftmost_tick,
                numbers_with_elongated_ticks=self.x_labeled_nums,
                color=self.axes_color
            )
            x_axis.shift(self.graph_origin - x_axis.number_to_point(0))
            if len(self.x_labeled_nums) > 0:
                if self.exclude_zero_label:
                    self.x_labeled_nums = [x for x in self.x_labeled_nums if x != 0]
                x_axis.add_numbers(*self.x_labeled_nums)
            x_label = TextMobject("$\\Omega_{L}$")
            x_label.next_to(x_axis.get_tick_marks(), UP + RIGHT,buff=SMALL_BUFF)
            x_label.shift_onto_screen()
            x_axis.add(x_label)
            self.x_axis_label_mob = x_label
            self.play(Write(x_axis))

        def add_y_axis(self):
            if self.y_labeled_nums is None:
                self.y_labeled_nums = []
            if self.y_bottom_tick is None:
                self.y_bottom_tick = self.y_min
            y_axis = NumberLine(
                x_min=self.y_min,
                x_max=self.y_max,
                unit_size=self.space_unit_to_y,
                tick_frequency=self.y_tick_frequency,
                leftmost_tick=self.y_bottom_tick,
                numbers_with_elongated_ticks=self.y_labeled_nums,
                color=self.axes_color,
                line_to_number_vect=LEFT,
                label_direction=LEFT,
            )
            y_axis.shift(self.graph_origin - y_axis.number_to_point(0))
            y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))
            if len(self.y_labeled_nums) > 0:
                if self.exclude_zero_label:
                    self.y_labeled_nums = [y for y in self.y_labeled_nums if y != 0]
                y_axis.add_numbers(*self.y_labeled_nums)
            y_label = TextMobject("$H_{LP}$")
            y_label.next_to(y_axis.get_corner(UP + RIGHT), UP + RIGHT,buff=SMALL_BUFF)
            y_label.shift_onto_screen()
            y_axis.add(y_label)
            self.y_axis_label_mob = y_label
            self.play(Write(y_axis))

        add_x_axis(self)
        self.x_axis.add(x_texts_2)
        add_y_axis(self)
        self.y_axis.add(y_texts)
        self.play(FadeOut(text_1))
        self.play(ShowCreation(graph_3,run_time=4),ShowCreation(graph_4,run_time=4))
        self.wait(3)

        #self.play(ShowCreation(number_line_1,run_time=2))
        #number_line_1.add(x_texts)
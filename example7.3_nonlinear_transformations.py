from manimlib.imports import *
class SimpleNonLinearTransform(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        self.play(ShowCreation(grid))
        self.play(FadeIn(circle))
        self.wait(2)

        nonLinear_Transform = lambda coordinate: coordinate + \
            np.array([np.sin(coordinate[0])**2, np.sin(coordinate[1]**3),0,])
        grid.prepare_for_nonlinear_transform() 
        
        self.play(grid.apply_function, nonLinear_Transform,
                  circle.apply_function, nonLinear_Transform, run_time=3)
        self.wait(2)

class ButterFly(Scene):
    def construct(self):
            butterfly = ParametricFunction(
            lambda t: np.array([
               (np.sin(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
               (np.cos(TAU*t))*(np.exp(np.cos(TAU*t)) - 2*np.cos(4*t*TAU) - np.power(np.sin((t*TAU)/12), 5)),
                0
            ]),
             t_min = 0, t_max = 40, step_size = 0.04, color = BLUE
            )
            self.play(ShowCreation(butterfly),run_time=5)
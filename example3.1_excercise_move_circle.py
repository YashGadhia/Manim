from manimlib.imports import *

class MoveCircleExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        ### Move circle to (3,3)
        square.shift(2*LEFT+2*DOWN)
        self.play(ShowCreation(circle), ShowCreation(square))
        self.wait(2) 


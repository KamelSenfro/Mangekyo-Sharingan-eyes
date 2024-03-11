#Mangekyo Sharingan eyes
from manim import *
import os
class Sharingan(Scene):
    def construct(self):
        # Parameters
        radius = 1
        distance_between = 0.5
        angle = 45  # in degrees

        # Ellipse 1
        ellipse1 = Ellipse(width=2*radius, height=radius, color=RED)
        ellipse1.shift(LEFT * distance_between / 2)
        ellipse1.rotate(angle * DEGREES)

        # Ellipse 2
        ellipse2 = Ellipse(width=2*radius, height=radius, color=RED)
        ellipse2.shift(RIGHT * distance_between / 2)
        ellipse2.rotate(-angle * DEGREES)

        self.play(Create(ellipse1), Create(ellipse2))
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = " ".join(["-p", module_name, "Sharingan"])
    os.system(f"manim {command}")

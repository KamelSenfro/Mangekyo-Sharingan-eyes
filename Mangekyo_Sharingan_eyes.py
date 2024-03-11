from manim import *

class Sharingan(Scene):
    def construct(self):
        # Parameters
        radius = 1
        distance_between = 8
        angle = 45  # in degrees
        inner_radius = 0.5  # Radius of the inner ellipses

        # Ellipse 1
        ellipse1 = Ellipse(width=2*radius, height=radius, fill_color=WHITE, fill_opacity=0.5, stroke_color=WHITE, stroke_width=4)
        ellipse1.shift(LEFT * distance_between / 2)
        ellipse1.rotate(angle * DEGREES)

        # Ellipse 2
        ellipse2 = Ellipse(width=2*radius, height=radius, fill_color=WHITE, fill_opacity=0.5, stroke_color=WHITE, stroke_width=4)
        ellipse2.shift(RIGHT * distance_between / 2)
        ellipse2.rotate(-angle * DEGREES)

        # Flip horizontally
        self.play(Create(ellipse1), Create(ellipse2))
        self.wait()
        self.play(Rotate(ellipse1, -180*DEGREES, about_point=ORIGIN))
        self.play(Rotate(ellipse2, 180*DEGREES, about_point=ORIGIN))

     
        update_func1 = lambda mob: mob.move_to(ellipse1.get_center())
        update_func2 = lambda mob: mob.move_to(ellipse2.get_center())

        inner_ellipse1 = Ellipse(width=1.7*radius, height=inner_radius, fill_color=GRAY_B, fill_opacity=0.0,stroke_color=WHITE, stroke_width=2)
        inner_ellipse1.add_updater(update_func1)
        inner_ellipse1.rotate(angle * DEGREES)

        inner_ellipse2 = Ellipse(width=1.7*radius, height=inner_radius, fill_color=GRAY_B, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2)
        inner_ellipse2.add_updater(update_func2)
        inner_ellipse2.rotate(-angle * DEGREES)
        
        # Red circles inside inner ellipses
        red_circle1 = Circle(radius=radius, color=RED, stroke_color=BLACK, stroke_width=1)
        red_circle1.move_to(inner_ellipse1)

        red_circle2 = Circle(radius=radius, color=RED, stroke_color=BLACK, stroke_width=1)
        red_circle2.move_to(inner_ellipse2)
        self.play(FadeIn(inner_ellipse1), FadeIn(inner_ellipse2), run_time=2)
        self.wait(1)

        
        
        self.play(Create(red_circle1), Create(red_circle2))
#lazy export
# if __name__ == "__main__":
#     module_name = os.path.basename(__file__)
#     command = " ".join(["-p", module_name, "Sharingan"])
#     os.system(f"manim {command}")
#manim -pql Mangekyo_Sharingan_eyes.py Sharingan
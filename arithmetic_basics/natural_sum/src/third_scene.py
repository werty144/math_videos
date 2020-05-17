from manimlib.imports import *
from src.functions import line_up_text_mobjects, get_coords


class ThirdScene(Scene):
    def construct(self):
        # center = Dot()
        # self.play(ShowCreation(center))
        x = TextMobject('x', color=RED)
        y = TextMobject('y', color=BLUE)
        rbr = TextMobject(')')
        lbr = TextMobject('(')
        plus_sign = TextMobject('+')
        eq_sign = TextMobject('=')
        group = line_up_text_mobjects(lbr, x, plus_sign, y, rbr, eq_sign, distance=0.1)
        group.scale(2)
        group.center()
        self.play(FadeIn(group))
        self.play(MoveAlongPath(x, ParametricFunction(lambda t: clockwise_path()(get_coords(x), RIGHT * 3, t)), run_time=2))

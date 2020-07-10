from manimlib.imports import *
from src.functions import make_screen_frame


class Intro(Scene):
    def construct(self):
        infty = TextMobject('$\\infty$').scale(7)
        q = TextMobject('?').scale(7)
        self.play(FadeIn(infty))
        self.play(ReplacementTransform(infty, q), run_time=1.5)

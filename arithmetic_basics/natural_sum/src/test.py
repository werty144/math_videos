from manimlib.imports import *


class Introduction(Scene):
    def construct(self):
        self.camera.background_color = GREY
        self.camera.init_background()
        natural_numbers_string = TextMobject("Натуральные числа", height=1)
        natural_numbers_string.shift(UP * 3.3)
        self.play(Write(natural_numbers_string))
        self.wait(1)

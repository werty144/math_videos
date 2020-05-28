from manimlib.imports import *


class Captions(Scene):
    def construct(self):
        thank = TextMobject('Спасибо!').scale(1.5).set_color(BLUE)
        caption1 = TextMobject('Ангелине, за помощь с оформлением')
        caption2 = TextMobject('3blue1brown-у, за библиотеку')
        thank.align_on_border(UP)
        caption1.next_to(thank, DOWN, buff=LARGE_BUFF)
        caption2.next_to(caption1, DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(thank))
        self.play(FadeIn(caption1))
        self.wait(1)
        self.play(FadeIn(caption2))
        self.wait(2)

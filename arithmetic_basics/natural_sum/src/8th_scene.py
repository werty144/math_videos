from src.functions import *


class Scene8(Scene):
    def construct(self):
        plus_fun = TextMobject('(', '$x$', ' $+$ ', '$y$', ')', ' $+$ ', '$z$', ' $=$ ', '(', '$x$', ' $+$ ', '$y$', ')', ' $+$ ', '$z$',
                               arg_separator='')
        plus_fun.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        self.play(FadeIn(plus_fun))
        self.play(*move_brackets_animation(8, 12, 11, 14, plus_fun))
        plus1 = plus_fun.get_parts_by_tex('+')[0]
        plus2 = plus_fun.get_parts_by_tex('+')[1]
        plus3 = plus_fun.get_parts_by_tex('+')[2]
        plus4 = plus_fun.get_parts_by_tex('+')[3]
        overp1 = overscribe_text(plus1, '1')
        overp2 = overscribe_text(plus2, '2')
        overp3 = overscribe_text(plus3, '2')
        overp4 = overscribe_text(plus4, '1')
        self.play(FadeIn(overp1), FadeIn(overp2))
        self.play(FadeIn(overp3), FadeIn(overp4))
        self.wait(1)
        draw_reference(self, 'Свойство сложения\\\\'
                             '$(x + y) + z = x + (y + z)$\\\\'
                             'называется \\underline{ассоциативность}')
        self.wait(2)

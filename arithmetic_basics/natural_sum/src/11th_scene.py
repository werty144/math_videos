from src.functions import *


class Scene11(Scene):
    def construct(self):
        equation1 = TextMobject('(', '(', '$a$', ' $+$ ', '$b$', ')', ' $+$ $c$', ')', ' $+$ $d$', ' ', '$=$',
                                arg_separator='')
        equation2 = TextMobject('$=$ ', '(', '(', '$a$', ' $+$ ', '$b$', ')', ' $+$ $c$', ')', ' $+$ $d$', ' $=$',
                                arg_separator='')
        equation2.shift(equation1.submobjects[-1].get_center() - equation2.submobjects[0].get_center())
        group1 = Group(equation1, equation2)
        group1.center()
        self.play(FadeIn(group1))
        self.play(*move_brackets_animation(2, 6, 5, 7, equation2))
        self.play(FadeIn(equation2.submobjects[2]))

        equation3 = TextMobject('$=$ ', '(', '$a$', ' $+$ ', '(', '$b$', ' $+$ $c$', ')', ')', ' $+$ $d$', ' $=$',
                                arg_separator='')
        equation3.shift(equation1.get_left() - equation3.get_left(), DOWN * 0.5)
        self.play(get_move_group_animation(group1, UP * 0.5), FadeIn(equation3))
        self.play(*move_brackets_animation(1, 8, 4, 9, equation3))

        equation4 = TextMobject('$=$ ', '$a$', ' $+$ ', '(', '(', '$b$', ' $+$ ', '$c$', ')', ' $+$ $d$', ')',
                                arg_separator='')
        equation4.shift(equation3.submobjects[-1].get_center() - equation4.submobjects[0].get_center())
        self.play(FadeIn(equation4))
        self.play(*move_brackets_animation(4, 8, 7, 9, equation4))

        self.play(get_move_group_animation(equation1, ORIGIN - equation1.submobjects[-1].get_center()),
                  get_move_group_animation(equation4, ORIGIN - equation4.submobjects[0].get_center()),
                  FadeOut(equation3),
                  FadeOut(equation2))
        self.wait(2)

from src.functions import *


class Scene11(Scene):
    def construct(self):
        statement = TextMobject('(', '(', '$a$', ' $+$ ', '$b$', ')', ' $+$ ', '$c$', ')', ' $+$ ', '$d$', ' ', '$=$ ',
                                '$a$', ' $+$ ', '(', '(', '$b$', ' $+$ ', '$c$', ')', ' $+$ ', '$d$', ')',
                                arg_separator='')
        statement.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE, 'd': ORANGE})
        statement.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        statement.scale(1.2)
        statement.align_on_border(UP)
        q_mark = overscribe_text(statement.submobjects[12], '?')
        self.play(FadeIn(statement))
        self.play(FadeIn(q_mark))

        equation1 = TextMobject('(', '(', '$a$', ' $+$ ', '$b$', ')', ' $+$ ', '$c$', ')', ' $+$ ', '$d$', ' ', '$=$',
                                arg_separator='')
        equation1.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE, 'd': ORANGE})
        equation2 = TextMobject('(', '(', '$a$', ' $+$ ', '$b$', ')', ' $+$ ', '$c$', ')', ' $+$ ', '$d$',
                                arg_separator='')
        equation2.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE, 'd': ORANGE})
        equation2.shift(equation1.get_right() - equation2.get_left() + RIGHT * space_width)
        group1 = Group(equation1, equation2)
        group1.center()
        self.play(FadeIn(Group(*equation1.submobjects[:-1])))
        self.play(FadeIn(equation2), FadeIn(equation1.submobjects[-1]))
        self.play(*move_brackets_animation(1, 5, 4, 7, equation2))

        equation3 = TextMobject('$=$ ', '(', '$a$', ' $+$ ', '(', '$b$', ' $+$ ', '$c$', ')', ')', ' $+$ ', '$d$',
                                arg_separator='')
        equation3.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE, 'd': ORANGE})
        equation3.shift(equation1.get_left() - equation3.get_left(), DOWN * 0.5)
        self.play(get_move_group_animation(group1, UP * 0.5))
        eq = TextMobject('$=$')
        eq.shift(equation2.get_right() - eq.get_left() + RIGHT * space_width)
        self.play(FadeIn(equation3), FadeIn(eq))
        self.play(*move_brackets_animation(1, 9, 4, 11, equation3))

        equation4 = TextMobject('$=$ ', '$a$', ' $+$ ', '(', '(', '$b$', ' $+$ ', '$c$', ')', ' $+$ ', '$d$', ')',
                                arg_separator='')
        equation4.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE, 'd': ORANGE})
        equation4.shift(equation3.get_right() - equation4.get_left() + RIGHT * space_width)
        self.play(FadeIn(equation4))
        self.play(*move_brackets_animation(4, 8, 7, 10, equation4))

        self.play(get_move_group_animation(equation1, ORIGIN - equation1.submobjects[-1].get_center()),
                  get_move_group_animation(equation4, ORIGIN - equation4.submobjects[0].get_center()),
                  FadeOut(equation3),
                  FadeOut(equation2),
                  FadeOut(eq))

        tick = TextMobject('\\checkmark')
        tick.set_color_by_tex('checkmark', GREEN)
        tick.set_height(q_mark.get_height())
        tick.shift(q_mark.get_bottom() - tick.get_bottom())
        self.play(ReplacementTransform(q_mark, tick))
        self.wait(2)

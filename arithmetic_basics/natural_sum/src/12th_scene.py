from src.functions import *


class Scene12(Scene):
    def construct(self):
        self.camera.background_color = RED
        statement = TextMobject('$a$', ' $+$ ', '$b$', ' $+$ ', '$c$', ' $=$ ',  '$b$', ' $+$ ', '$c$', ' $+$ ', '$a$',
                                arg_separator='')
        statement.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        statement.scale(1.3)
        statement.align_on_border(UP)
        q_mark = overscribe_text(statement.submobjects[5], '?')
        self.play(FadeIn(statement))
        self.play(FadeIn(q_mark))
        part1 = TextMobject('$a$', ' $+$ ', '$b$', ' $+$ ', '$c$', ' $=$', arg_separator='')
        part1.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        part2 = TextMobject('(', '$a$', ' $+$ ', '$b$', ')', ' $+$ ', '$c$', ' $=$', arg_separator='')
        part2.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        part2.shift(part1.get_right() - part2.get_left(), RIGHT * space_width,
                    DOWN * (part2.submobjects[1].get_bottom()[1] - part1.submobjects[0].get_bottom()[1]))
        part3 = TextMobject('(', '$b$', ' $+$ ', '$a$', ')', ' $+$ ', '$c$', arg_separator='')
        part3.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        part3.shift(part2.get_right() - part3.get_left() + RIGHT * space_width)
        group1 = Group(part1, part2, part3).center()
        self.play(FadeIn(Group(*part1.submobjects[:-1])))
        self.play(FadeIn(part1.submobjects[-1]), FadeIn(Group(*part2.submobjects[:-1])))
        self.play(*swap_variables_animation(1, 3, part2))
        self.play(FadeIn(part2.submobjects[-1]), FadeIn(part3))
        self.play(*move_brackets_animation(0, 4, 3, 6, part3))

        eq = TextMobject('$=$')
        eq.shift(part3.get_right() - eq.get_left(), RIGHT * space_width)
        part4 = TextMobject('$=$ ', '$b$', ' $+$ ', '(', '$a$',  ' $+$ ', '$c$', ')', arg_separator='')
        part4.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        part4.shift(part1.get_left() - part4.get_left(), DOWN * 0.5)
        self.play(
            get_move_group_animation(group1, UP * 0.5),
        )
        self.play(FadeIn(part4), FadeIn(eq))
        self.play(*swap_variables_animation(4, 6, part4))

        part5 = TextMobject('$=$ ', '$b$', ' $+$ ', '(', '$c$', ' $+$ ', '$a$', ')', arg_separator='')
        part5.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        part5.shift(part4.get_right() - part5.get_left(), RIGHT * space_width)
        part5.shift(DOWN * (part5.submobjects[1].get_bottom()[1] - part4.submobjects[1].get_bottom()[1]))
        self.play(FadeIn(part5))
        self.play(*move_brackets_animation(3, 7, 1, 4, part5))

        part6 = TextMobject('$=$ ', '$b$', ' $+$ ', '$c$', ' $+$ ', '$a$', arg_separator='')
        part6.set_color_by_tex_to_color_map({'a': RED, 'b': GREEN, 'c': BLUE})
        part6.shift(part5.get_right() - part6.get_left(), RIGHT * space_width)
        self.play(FadeIn(part6))

        tick = TextMobject('\\checkmark')
        tick.set_color_by_tex('checkmark', GREEN)
        tick.set_height(q_mark.get_height())
        tick.shift(q_mark.get_bottom() - tick.get_bottom())

        self.play(FadeOut(part2),
                  FadeOut(part3),
                  FadeOut(part4),
                  FadeOut(part5),
                  FadeOut(eq),
                  get_move_group_animation(part1, ORIGIN - part1.submobjects[-1].get_center()),
                  get_move_group_animation(part6, ORIGIN - part6.submobjects[0].get_center())
                  )
        self.play(ReplacementTransform(q_mark, tick))
        self.wait(2)

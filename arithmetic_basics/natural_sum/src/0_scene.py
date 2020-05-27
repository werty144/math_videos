from src.functions import *


def get_to_dot_vector(group, bullet_list, dot_ind):
    dot = bullet_list.submobjects[dot_ind]
    return dot.get_left() - group.get_left() + RIGHT * MED_LARGE_BUFF


class Scene0(Scene):
    def construct(self):
        bullet_list = My_bullet_list(6)
        bullet_list.align_on_border(UL)
        bullet_list.shift(DOWN * 0.3)

        peremena_mest = TextMobject('$x$', ' $+$ ', '$y$', ' $=$ ', '$x$', ' $+$ ', '$y$', arg_separator='')
        q1 = overscribe_text(peremena_mest.submobjects[3], '?')
        peremena_mest.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE})

        self.play(FadeIn(peremena_mest))
        self.play(*swap_variables_animation(4, 6, peremena_mest), run_time=1.5)
        self.play(FadeIn(q1))
        self.wait(1)
        self.play(get_move_group_animation(Group(peremena_mest, q1), get_to_dot_vector(peremena_mest, bullet_list, 0)),
                  bullet_list.fade_in_dot_animation(0))
        self.wait(1)

        # time passed: 6.5

        zero_division = TextMobject('$\\frac{1}{0}$ ', '\\xmark').scale(1.3)
        zero_division.set_color_by_tex_to_color_map({'xmark': "#cc3333"})
        self.play(FadeIn(zero_division))
        self.wait(1.5)
        self.play(get_move_group_animation(zero_division, get_to_dot_vector(zero_division, bullet_list, 1)),
                  bullet_list.fade_in_dot_animation(1))
        self.wait(1)

        # time passed 11

        minus_on_minus = TextMobject('(', '$-$', ')',  ' $\\ast$ ', '(', '$-$', ')', ' $=$ ', '$+$', arg_separator='')
        q2 = overscribe_text(minus_on_minus.submobjects[7], '?')
        minus_on_minus.set_color_by_tex_to_color_map({'-': BLUE, '+': RED})

        self.play(FadeIn(minus_on_minus))
        self.play(FadeIn(q2))
        self.wait(1)
        self.play(
            get_move_group_animation(Group(minus_on_minus, q2), get_to_dot_vector(minus_on_minus, bullet_list, 2)),
            bullet_list.fade_in_dot_animation(2))
        self.wait(1)

        # time passed 16

        frac_eq = TextMobject(':',  '$\\frac{a}{b}$', '$=$', '$\\ast$', '$\\frac{b}{a}$')
        # frac_eq.set_color_by_tex_to_color_map({'{a}{b}': RED, '{b}{a}': BLUE})
        q3 = overscribe_text(frac_eq.submobjects[2], '?')
        self.play(FadeIn(frac_eq))
        self.play(FadeIn(q3))
        self.wait(1)
        self.play(
            get_move_group_animation(Group(frac_eq, q3), get_to_dot_vector(frac_eq, bullet_list, 3)),
            bullet_list.fade_in_dot_animation(3))
        self.wait(1)

        # time passed 21

        irr_pow = TextMobject('$5^{\\sqrt{2}}$ $=$ ',
                              '$\\underbrace{5 \\cdot 5 \\cdot \\ldots \\cdot 5}_{\\sqrt{2}?}$', arg_separator='')
        self.play(FadeIn(irr_pow.submobjects[0]))
        self.wait(4)
        self.play(FadeIn(irr_pow.submobjects[1]))
        self.wait(1)
        self.play(get_move_group_animation(irr_pow, get_to_dot_vector(irr_pow.submobjects[0].submobjects[0], bullet_list, 4)),
                  bullet_list.fade_in_dot_animation(4))
        self.wait(1)

        # time passed 30

        neg_root = TextMobject('$\\sqrt{-1}$', '$=$')
        q4 = overscribe_text(neg_root.submobjects[1], '?')
        neg_root.submobjects[0].submobjects[2].set_color(BLUE)
        self.play(FadeIn(neg_root))
        self.play(FadeIn(q4))
        self.wait(1)
        self.play(get_move_group_animation(Group(neg_root, q4), get_to_dot_vector(neg_root, bullet_list, 5)),
                  bullet_list.fade_in_dot_animation(5))

        # time passed 34

        self.wait(2)

        big_q_mark = TextMobject('?').scale(7)
        big_q_mark.shift(RIGHT * ((FRAME_X_RADIUS + irr_pow.get_right()[0]) / 2 - big_q_mark.get_center()[0]))
        over_q_mark = overscribe_text(big_q_mark, '?')

        self.play(FadeIn(big_q_mark))
        self.play(FadeIn(over_q_mark))

        self.wait(28.5)
        self.play(FadeOut(big_q_mark), FadeOut(over_q_mark))
        self.wait(0.5)
        quote = TextMobject('«Бог создал натуральные числа,\\\\ всё остальное – дело рук человека».\\\\')
        author = TextMobject('\\copyright \\space Л. Кронекер')
        quote.shift(RIGHT * ((FRAME_X_RADIUS + irr_pow.get_right()[0])/2 - quote.get_center()[0]), UP * 0.7)
        author.shift(quote.get_bottom() - author.get_top(), DOWN * 0.3)
        self.play(Write(quote, run_time=2.5))
        self.play(FadeIn(author))

        self.wait(3.5)

        fade_outs = []
        for obj in self.mobjects:
            fade_out = FadeOut(obj)
            fade_outs.append(fade_out)

        self.play(*fade_outs)

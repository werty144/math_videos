from src.functions import *


class Scene9(Scene):
    def construct(self):
        assos = TextMobject('$f($', '$f($', '$x$', ', ', '$y$', ')', ', ', '$z$', ')', ' $=$ ',
                            '$f($', '$x$', ', ', '$f($', '$y$', ', ', '$z$', ')', ')', arg_separator='')
        assos.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        eq = assos.submobjects[9]
        q_mark = overscribe_text(eq, '?')
        self.wait(3)
        self.play(Write(assos), run_time=2)
        self.play(FadeIn(q_mark))
        self.wait(5)
        sum_n_sq_func = TextMobject('$f($', '$x$', ', ', '$y$', ')', ' $=$ ', '(', '$x$', ' $+$ ', '$y$', '$)^2$', arg_separator='')
        sum_n_sq = TextMobject('(', '$x$', ' $+$ ', '$y$', '$)^2$', arg_separator='')
        sum_n_sq.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        sum_n_sq_func.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        sum_n_sq_func.scale(1.3)
        sum_n_sq_func.align_on_border(UP)
        self.play(FadeIn(sum_n_sq_func))

        # time passed 12

        self.wait(4)

        left_inner = Group(*assos.submobjects[1:6])
        sum_n_sq_for_left_inner = sum_n_sq.copy()
        sum_n_sq_for_left_inner.shift(left_inner.get_center() - sum_n_sq.get_center()).set_width(left_inner.get_width())

        right_inner = Group(*assos.submobjects[13:18])
        sum_n_sq_for_right_inner = TextMobject('(', '$y$', ' $+$ ', '$z$', '$)^2$', arg_separator='').center()
        sum_n_sq_for_right_inner.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        sum_n_sq_for_right_inner.shift(right_inner.get_center()).set_width(right_inner.get_width())

        self.play(ReplacementTransform(left_inner, sum_n_sq_for_left_inner), ReplacementTransform(right_inner, sum_n_sq_for_right_inner))
        self.wait(1)

        left_outer = TextMobject('(', '(', '$x$', ' $+$ ', '$y$', '$)^2$', ' $+$ ', '$z$', '$)^2$', arg_separator='')
        left_outer.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        left_outer.center().shift(Group(*assos.submobjects[0:9]).get_center() + LEFT * 0.2)
        self.remove(sum_n_sq_for_left_inner)

        right_outer = TextMobject('(',  '$x$', ' $+$ ', '(', '$y$', ' $+$ ', '$z$', '$)^2$', '$)^2$', arg_separator='')
        right_outer.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        right_outer.center().shift(Group(*assos.submobjects[10:19]).get_center() + RIGHT * 0.3)
        self.remove(sum_n_sq_for_right_inner)

        self.play(ReplacementTransform(Group(*assos.submobjects[0:9]), left_outer),
                  ReplacementTransform(Group(*assos.submobjects[10:19]), right_outer))
        self.wait(1)

        # time passed 20

        self.wait(5)

        self.play(*substitution_animation(2, '1', left_outer, self),
                  *substitution_animation(4, '2', left_outer, self),
                  *substitution_animation(7, '3', left_outer, self),
                  *substitution_animation(1, '1', right_outer, self),
                  *substitution_animation(4, '2', right_outer, self),
                  *substitution_animation(6, '3', right_outer, self))

        self.wait(1)

        left_val = TextMobject('144')
        right_val = TextMobject('676')
        left_val.shift(eq.get_left() - left_val.get_right() + LEFT * space_width)
        right_val.shift(eq.get_right() - right_val.get_left() + RIGHT * space_width)
        neq = TextMobject('$\\neq$')
        neq.set_color_by_tex('neq', RED)
        neq.shift(eq.get_center() - neq.get_center())
        self.play(ReplacementTransform(right_outer, right_val),
                  ReplacementTransform(left_outer, left_val),
                  ReplacementTransform(eq, neq),
                  FadeOut(q_mark),
                  run_time=2
                  )

        self.wait(2)

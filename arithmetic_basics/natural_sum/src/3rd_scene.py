from manimlib.imports import *
from src.functions import get_coords, get_move_group_animation, make_screen_frame


class Scene3(Scene):
    def construct(self):
        equation = TextMobject('$x$', '+', '$y$', '=', '$y$', '+', '$x$', arg_separator=' ')
        equation.set_color_by_tex_to_color_map({'$x$': RED, '$y$': BLUE})
        equation.scale(2)
        x1 = equation.get_parts_by_tex('$x$')[0]
        plus_sign1 = equation.get_parts_by_tex('+')[0]
        y1 = equation.get_parts_by_tex('$y$')[0]
        eq_sign = equation.get_part_by_tex('=')
        x2 = equation.get_parts_by_tex('$x$')[1]
        plus_sign2 = equation.get_parts_by_tex('+')[1]
        y2 = equation.get_parts_by_tex('$y$')[1]

        left_side = TextMobject('$x$', '+', '$y$')
        left_side.set_color_by_tex_to_color_map({'$x$': RED, '$y$': BLUE})
        left_side.scale(2)
        self.play(FadeIn(left_side))
        left_side_center = Group(x1, plus_sign1, y1).get_center()
        self.play(get_move_group_animation(left_side, left_side_center - left_side.get_center()), run_time=1.5)
        x1_copy = x1.copy()
        y1_copy = y1.copy()
        plus_sign1_copy = plus_sign1.copy()
        eq_sign_copy = eq_sign.copy()
        x_movement = MoveAlongPath(x1_copy, ParametricFunction(
            lambda t: clockwise_path()(get_coords(x1), get_coords(x2), t)
        ))
        plus_movement = MoveAlongPath(plus_sign1_copy, ParametricFunction(
            lambda t: clockwise_path()(get_coords(plus_sign1), get_coords(plus_sign2), t)
        ))
        y_movement = MoveAlongPath(y1_copy, ParametricFunction(
            lambda t: clockwise_path()(get_coords(y1), get_coords(y2), t)
        ))
        self.play(x_movement, plus_movement, y_movement, FadeIn(eq_sign_copy), run_time=2)
        self.remove(x1_copy, y1_copy, plus_sign1_copy, eq_sign_copy, left_side)
        self.add(equation)
        self.wait(1)
        scale_factor = 0.7
        self.play(ScaleInPlace(equation, scale_factor),
                  get_move_group_animation(equation,
                                           equation.copy().scale(scale_factor).align_on_border(UL).get_center()))
        self.wait(1)


from manimlib.imports import *
from src.functions import *


def get_equation():
    equation = TextMobject('$x$', '+', '$y$', '=', '$y$', '+', '$x$', arg_separator=' ')
    equation.set_color_by_tex_to_color_map({'$x$': RED, '$y$': BLUE})
    equation.scale(1.4)
    equation.align_on_border(UL)
    return equation


class Scene4(Scene):
    def construct(self):
        equation = get_equation()
        self.add(equation)
        chain = TextMobject('$plus$', '(', '$x$', ',', ' ', '$y$', ')',
                            ' = ', '$x$', ' + ', '$y$', ' = ', '$y$', ' + ', '$x$', ' = ',
                            '$plus$', '(', '$y$', ',', ' ', '$x$', ')',
                            arg_separator='')
        chain.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE})
        scale_factor = 1.5
        chain.scale(scale_factor)
        left_func = Group(
            chain.get_part_by_tex('$plus$'),
            chain.get_part_by_tex('('),
            chain.get_part_by_tex('$x$'),
            chain.get_part_by_tex(','),
            chain.get_part_by_tex(' ', substring=False),
            chain.get_part_by_tex('$y$'),
            chain.get_part_by_tex(')'),
        )
        eq1 = chain.get_part_by_tex(' = ')
        left_sum = Group(
            chain.get_parts_by_tex('$x$')[1],
            chain.get_part_by_tex('+'),
            chain.get_parts_by_tex('$y$')[1],
        )
        eq2 = chain.get_parts_by_tex(' = ')[1]
        right_sum = Group(
            chain.get_parts_by_tex('$x$')[2],
            chain.get_parts_by_tex('+')[1],
            chain.get_parts_by_tex('$y$')[2],
        )
        eq3 = chain.get_parts_by_tex(' = ')[2]
        right_func = Group(
            chain.get_parts_by_tex('$plus$')[1],
            chain.get_parts_by_tex('(')[1],
            chain.get_parts_by_tex('$x$')[3],
            chain.get_parts_by_tex(',')[1],
            chain.get_parts_by_tex(' ', substring=False)[1],
            chain.get_parts_by_tex('$y$')[3],
            chain.get_parts_by_tex(')')[1],
        )
        left_func_copy = left_func.copy()
        left_func_copy.center()
        self.play(FadeIn(left_func_copy[0]))
        self.play(*[FadeIn(elem) for elem in left_func_copy[1:]])
        self.play(get_move_group_animation(left_func_copy, left_func.get_center()))
        self.add(left_func)
        self.remove(left_func_copy)
        self.play(FadeIn(eq1))
        self.play(FadeIn(left_sum))
        self.play(FadeIn(eq2))
        self.play(FadeIn(right_sum))
        self.play(FadeIn(eq3))
        self.play(FadeIn(right_func))
        left_func_with_eq = Group(left_func, eq1)
        right_func_with_eq = Group(right_func, eq3)
        move_left = get_move_group_animation(left_func_with_eq, -eq1.get_center())
        move_right = get_move_group_animation(right_func_with_eq, -eq3.get_center())
        self.play(move_left, move_right, FadeOut(eq2), FadeOut(left_sum), FadeOut(right_sum))
        eq = eq1.copy()
        self.add(eq)
        self.remove(eq1, eq3)
        self.wait(1)

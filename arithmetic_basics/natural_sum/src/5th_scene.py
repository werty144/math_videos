from src.functions import *


def create_put_onto_equation(scene, type1, type2, type1_color, type2_color):
    scene.set_camera_orientation(phi=-PI / 10)
    put_on_func = TextMobject('$putOnto$', '(', '\\quad', ',', '\\quad', ')', '$=$', arg_separator='')
    scene.camera.add_fixed_orientation_mobjects(put_on_func)
    lbr = put_on_func.get_part_by_tex('(')
    rbr = put_on_func.get_part_by_tex(')')
    commma = put_on_func.get_part_by_tex(',')
    arg1_figure = type1(**drawing_defaults, fill_color=type1_color)
    arg2_figure = type2(**drawing_defaults, fill_color=type2_color)
    gap1 = (commma.get_left() - lbr.get_right())[0]
    gap2 = (rbr.get_left() - commma.get_right())[0]
    arg1_figure.set_width(gap1 * 0.7)
    arg2_figure.set_width(gap2 * 0.7)
    arg1_figure.next_to(lbr, RIGHT * (lbr.get_width() / 2 + arg1_figure.get_width() / 2))
    arg2_figure.next_to(rbr, LEFT * (rbr.get_width() / 2 + arg2_figure.get_width() / 2))
    only_func = Group(
        put_on_func.get_part_by_tex('putOnto'),
        put_on_func.get_part_by_tex('('),
        put_on_func.get_part_by_tex('\\quad'),
        put_on_func.get_part_by_tex(','),
        put_on_func.get_parts_by_tex('\\quad')[1],
        put_on_func.get_part_by_tex(')')
    )
    eq = put_on_func.get_part_by_tex('=')

    scene.play(FadeIn(arg2_figure), FadeIn(only_func), FadeIn(arg1_figure))
    scene.play(FadeIn(eq))
    group = Group(eq, only_func, arg1_figure, arg2_figure)
    scene.play(get_move_group_animation(group, ORIGIN - eq.get_center()))

    figure2 = arg2_figure.copy()
    scene.add(figure2)
    figure1 = arg1_figure.copy()
    scene.add(figure1)
    figure1_shift_vector = eq.get_center() + \
                           RIGHT * (eq.get_width() + 4 * math.sqrt(2) * figure1.get_width() / 2) + \
                           DOWN * (figure2.get_height() * 2) - \
                           figure1.get_center()
    scene.play(ScaleInPlace(figure1, 4), get_move_group_animation(figure1, figure1_shift_vector))
    center_should = get_onto_center_should(figure2.copy().scale(4), figure1)
    scene.play(ScaleInPlace(figure2, 4), put_onto_animation(figure2, center_should))

    def rotate_updater(mobject: Mobject, dt, rate=0.1):
        return mobject.rotate_in_place(rate * PI * dt, Y_AXIS)

    figure1.add_updater(rotate_updater)
    figure2.add_updater(rotate_updater)

    return Group(only_func, eq, arg1_figure, arg2_figure, figure1, figure2)


class Scene5(SpecialThreeDScene):
    def construct(self):
        group1 = create_put_onto_equation(self, Cube, Pyramid, BLUE, GREEN)
        group1_future_center = group1.get_center() + LEFT * ((group1.get_right() - ORIGIN)[0] + 1)
        self.wait(2)
        self.play(move_to_border_and_scale_animation(group1, UL, 0.5))
        group2 = create_put_onto_equation(self, Pyramid, Cube, GREEN, BLUE)
        self.wait(2)
        eq2 = group2[1]
        future_eq2_center = eq2.get_center() + RIGHT * (group2[4].get_x() - eq2.get_x()) * 2
        func2 = Group(group2[0], group2[2], group2[3])
        future_func2_center = func2.get_center() + RIGHT * (group2[4].get_x() - func2.get_x()) * 2
        eq2_movement = MoveAlongPath(eq2, ParametricFunction(
            lambda t: counterclockwise_path()(eq2.get_center(), future_eq2_center, t)
        ))
        func2_movement = MoveAlongPath(func2, ParametricFunction(
            lambda t: counterclockwise_path()(func2.get_center(), future_func2_center, t)
        ))
        self.play(eq2_movement, func2_movement)
        group2_shift = RIGHT - group2.get_left()
        self.play(ScaleInPlace(group1, 2),
                  get_move_group_animation(group1, group1_future_center - group1.get_center()),
                  get_move_group_animation(group2, group2_shift))
        neq = TextMobject('$\\neq$')
        neq.set_color_by_tex_to_color_map({'$\\neq$': RED})
        self.camera.add_fixed_orientation_mobjects(neq)
        neq.scale(2)
        neq.center()
        self.play(FadeIn(neq))
        self.wait(2)
        group1_final_shift = ORIGIN - group1[1].get_center()
        group2_final_shift = ORIGIN - group2[1].get_center()
        right_side = Group(group1[0], group1[2], group1[3]).copy()
        left_side = Group(group2[0], group2[2], group2[3]).copy()
        self.add(right_side, left_side)
        self.remove(group1[0], group1[2], group1[3], group2[0], group2[2], group2[3])
        self.play(ScaleInPlace(neq, 0.5),
                  get_move_group_animation(right_side, group1_final_shift),
                  get_move_group_animation(left_side, group2_final_shift),
                  FadeOut(group2[4]),
                  FadeOut(group2[5]),
                  FadeOut(group1[4]),
                  FadeOut(group1[5]),
                  FadeOut(group1[1]),
                  FadeOut(group2[1])
                  )
        self.wait(2)

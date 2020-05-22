from src.functions import *


def create_put_onto_equation(scene, type1, type2):
    make_screen_frame(scene)
    scene.set_camera_orientation(phi=-PI / 10)
    put_on_func = TextMobject('$putOnto$', '(', '\\quad', ',', '\\quad', ')', '$=$', arg_separator='')
    scene.camera.add_fixed_orientation_mobjects(put_on_func)
    lbr = put_on_func.get_part_by_tex('(')
    rbr = put_on_func.get_part_by_tex(')')
    commma = put_on_func.get_part_by_tex(',')
    arg1_figure = type1(**drawing_defaults)
    arg2_figure = type2(**drawing_defaults, fill_color=GREEN)
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
    figure1_shift_vector = eq.get_center() + RIGHT * (
            eq.get_width() + 4 * math.sqrt(2) * figure1.get_width() / 2) - figure1.get_center()
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
        group1 = create_put_onto_equation(self, Cube, Pyramid)
        self.wait(2)
        self.play(move_to_border_and_scale_animation(group1, UL, 0.5))
        create_put_onto_equation(self, Pyramid, Cube)
        self.wait(2)

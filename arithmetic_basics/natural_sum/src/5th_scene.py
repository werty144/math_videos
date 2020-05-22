from src.functions import *


class Scene5(SpecialThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=-PI / 10)
        put_on_func = TextMobject('$putOnto$', '(', '\\quad', ',', '\\quad', ')', '$=$', arg_separator='')
        self.camera.add_fixed_orientation_mobjects(put_on_func)
        lbr = put_on_func.get_part_by_tex('(')
        rbr = put_on_func.get_part_by_tex(')')
        arg_cube = Cube(side_length=lbr.get_height() * 0.8,
                        **drawing_defaults)
        arg_pyramid = Pyramid(**drawing_defaults, fill_color=GREEN)
        arg_pyramid.set_width(arg_cube.get_width())
        arg_cube.next_to(lbr, RIGHT * (lbr.get_width() / 2 + arg_cube.get_width() / 2))
        arg_pyramid.next_to(rbr, LEFT * (rbr.get_width() / 2 + arg_pyramid.get_width() / 2))
        only_func = Group(
            put_on_func.get_part_by_tex('putOnto'),
            put_on_func.get_part_by_tex('('),
            put_on_func.get_part_by_tex('\\quad'),
            put_on_func.get_part_by_tex(','),
            put_on_func.get_parts_by_tex('\\quad')[1],
            put_on_func.get_part_by_tex(')')
        )
        eq = put_on_func.get_part_by_tex('=')

        self.play(FadeIn(arg_pyramid), FadeIn(only_func), FadeIn(arg_cube))
        pyramid = arg_pyramid.copy()
        self.add(pyramid)
        cube = arg_cube.copy()
        self.add(cube)
        self.play(FadeIn(eq))
        cube_shift_vector = eq.get_center() + RIGHT * (eq.get_width() + 4 * math.sqrt(2) * cube.get_width() / 2) - cube.get_center()
        self.play(ScaleInPlace(cube, 4), get_move_group_animation(cube, cube_shift_vector))
        center_should = get_center_should(pyramid.copy().scale(4), cube)
        self.play(ScaleInPlace(pyramid, 4), get_move_group_animation(pyramid, center_should - pyramid.get_center()))

        def rotate_updater(mobject: Mobject, dt, rate=0.1):
            return mobject.rotate_in_place(rate * PI * dt, Y_AXIS)

        cube.add_updater(rotate_updater)
        pyramid.add_updater(rotate_updater)
        self.wait(2)

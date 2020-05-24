from src.functions import *


def get_three_cubes():
    cube1 = Cube(fill_color=GREEN, side_length=1, **drawing_defaults)
    cube1.shift(RIGHT)
    cube2 = Cube(fill_color=GREEN, side_length=1, **drawing_defaults)
    cube2.shift(RIGHT * 2.5)
    cube3 = Cube(fill_color=GREEN, side_length=1, **drawing_defaults)
    cube3.shift(RIGHT * 4)
    return Group(cube1, cube2, cube3)


def get_two_cubes():
    cube4 = Cube(fill_color=BLUE, side_length=1, **drawing_defaults)
    cube4.shift(LEFT)
    cube5 = Cube(fill_color=BLUE, side_length=1, **drawing_defaults)
    cube5.shift(LEFT * 2.5)
    return Group(cube4, cube5)


def make_ellipse(scene, center=ORIGIN, width=11, height=4):
    ellipse = Ellipse(width=width, height=height, stroke_color=WHITE)
    scene.add_fixed_in_frame_mobjects(ellipse)
    ellipse.shift(center)
    scene.play(DrawBorderThenFill(ellipse))
    scene.remove(ellipse)


class Scene10(SpecialThreeDScene):
    def construct(self):
        make_screen_frame(self)
        self.set_camera_orientation(phi=PI/3)
        giant_lbr = TextMobject('(').set_height(3)
        giant_rbr = TextMobject(')').set_height(3)
        self.camera.add_fixed_orientation_mobjects(giant_rbr, giant_lbr)
        cubes2 = get_two_cubes()
        cubes3 = get_three_cubes()
        cube1 = Cube(fill_color=RED, side_length=1, **drawing_defaults)
        cube1.shift(LEFT * 4.5)
        cube_group = Group(cube1, cubes2, cubes3)
        cube_group.center()
        cube1_center = cube1.get_center()
        cubes2_center = cubes2.get_center()
        cubes3_center = cubes3.get_center()
        self.play(FadeIn(cube_group))

        giant_lbr.shift(cube1.get_left() - giant_lbr.get_right())
        giant_rbr.shift(cubes2.get_right() - giant_rbr.get_left())
        left_prior = TextMobject('(', '$x$', ' $+$ ', '$y$', ')', ' $+$ ', '$z$', arg_separator='')
        self.camera.add_fixed_orientation_mobjects(left_prior)
        left_prior.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        left_prior.scale(1.3)
        left_prior.shift(UP * 8)
        self.play(FadeIn(left_prior))
        self.play(FadeIn(giant_lbr), FadeIn(giant_rbr))
        self.play(*get_together_animation(cube1, cubes2))
        self.play(FadeOut(giant_rbr), FadeOut(giant_lbr))
        self.play(*get_together_animation(Group(cube1, cubes2), cubes3))
        make_ellipse(self)
        self.play(get_move_group_animation(cube1, cube1_center - cube1.get_center()),
                  get_move_group_animation(cubes2, cubes2_center - cubes2.get_center()),
                  get_move_group_animation(cubes3, cubes3_center - cubes3.get_center()),
                  FadeOut(left_prior)
                  )

        giant_lbr.shift(cubes2.get_left() - giant_lbr.get_right())
        giant_rbr.shift(cubes3.get_right() - giant_rbr.get_left())
        right_prior = TextMobject('$x$', ' $+$ ', '(', '$y$', ' $+$ ', '$z$', ')', arg_separator='')
        self.camera.add_fixed_orientation_mobjects(right_prior)
        right_prior.set_color_by_tex_to_color_map({'x': RED, 'y': BLUE, 'z': GREEN})
        right_prior.scale(1.3)
        right_prior.shift(UP * 8)
        self.play(FadeIn(right_prior))
        self.play(FadeIn(giant_lbr), FadeIn(giant_rbr))
        self.play(*get_together_animation(cubes2, cubes3))
        self.play(FadeOut(giant_rbr), FadeOut(giant_lbr))
        self.play(*get_together_animation(cube1, Group(cubes2, cubes3)))
        make_ellipse(self)
        self.play(get_move_group_animation(cube1, cube1_center - cube1.get_center()),
                  get_move_group_animation(cubes2, cubes2_center - cubes2.get_center()),
                  get_move_group_animation(cubes3, cubes3_center - cubes3.get_center()),
                  FadeOut(right_prior)
                  )
        self.wait(2)

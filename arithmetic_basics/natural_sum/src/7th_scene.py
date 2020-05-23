from src.functions import *


def get_three_cubes():
    cube1 = Cube(side_length=1, **drawing_defaults)
    cube1.shift(RIGHT)
    cube2 = Cube(side_length=1, **drawing_defaults)
    cube2.shift(RIGHT * 3)
    cube3 = Cube(side_length=1, **drawing_defaults)
    cube3.shift(RIGHT * 5)
    return Group(cube1, cube2, cube3)


def get_two_cubes():
    cube4 = Cube(fill_color=RED, side_length=1, **drawing_defaults)
    cube4.shift(LEFT * 5)
    cube5 = Cube(fill_color=RED, side_length=1, **drawing_defaults)
    cube5.shift(LEFT * 3)
    return Group(cube4, cube5)


def make_ellipse(scene):
    ellipse = Ellipse(width=11, height=4, stroke_color=WHITE)
    scene.add_fixed_in_frame_mobjects(ellipse)
    scene.play(DrawBorderThenFill(ellipse))
    scene.remove(ellipse)


class Scene7(SpecialThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI/3)
        two_cubes = get_two_cubes()
        three_cubes = get_three_cubes()
        self.play(FadeIn(two_cubes))
        self.play(FadeIn(three_cubes))
        self.play(get_move_group_animation(two_cubes, RIGHT), get_move_group_animation(three_cubes, LEFT))
        make_ellipse(self)
        self.play(get_move_group_animation(two_cubes, LEFT), get_move_group_animation(three_cubes, RIGHT))
        self.move_camera(theta=PI/2)
        self.play(get_move_group_animation(two_cubes, RIGHT), get_move_group_animation(three_cubes, LEFT))
        make_ellipse(self)


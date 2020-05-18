from manimlib.imports import *
from src.functions import my_title, get_move_group_animation


def get_three_cubes():
    cube1 = Cube(side_length=1, stroke_color=DARK_BLUE, stroke_width=DEFAULT_STROKE_WIDTH)
    cube1.shift(RIGHT)
    cube2 = Cube(side_length=1, stroke_color=DARK_BLUE, stroke_width=DEFAULT_STROKE_WIDTH)
    cube2.shift(RIGHT * 3)
    cube3 = Cube(side_length=1, stroke_color=DARK_BLUE, stroke_width=DEFAULT_STROKE_WIDTH)
    cube3.shift(RIGHT * 5)
    return Group(cube1, cube2, cube3)


def get_two_cubes():
    cube4 = Cube(fill_color=RED, side_length=1, stroke_color=DARK_BLUE, stroke_width=DEFAULT_STROKE_WIDTH)
    cube4.shift(LEFT * 5)
    cube5 = Cube(fill_color=RED, side_length=1, stroke_color=DARK_BLUE, stroke_width=DEFAULT_STROKE_WIDTH)
    cube5.shift(LEFT * 3)
    return Group(cube4, cube5)


class Scene2(SpecialThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=-PI * 5 / 3)

        title = my_title('Сложение', height=1, color=BLUE)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title, run_time=2))

        three_cubes = get_three_cubes()
        two_cubes = get_two_cubes()

        self.play(FadeIn(two_cubes))
        self.play(FadeIn(three_cubes))

        move_three = get_move_group_animation(three_cubes, LEFT)
        move_two = get_move_group_animation(two_cubes, RIGHT)
        self.play(move_two, move_three)

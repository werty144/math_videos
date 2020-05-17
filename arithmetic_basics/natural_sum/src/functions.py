import numpy
from manimlib.animation.movement import MoveAlongPath
from manimlib.imports import *
from manimlib.mobject.functions import ParametricFunction


def text_fit_to_box(text, box: Rectangle):
    lines_n = len(text.splitlines())
    text_obj = TextMobject(text, height=lines_n * 0.4)
    box.set_width(text_obj.get_width() + 0.2)
    text_obj.center()
    box.center()
    return text_obj


def draw_reference(scene, text):
    margin_right = 0.3
    margin_bot = 0.3
    box = Rectangle()
    box.set_stroke(color=RED)
    text_obj = text_fit_to_box(text, box)
    group = Group(box, text_obj)
    group.shift(np.array([FRAME_X_RADIUS - margin_right - box.get_width() * 0.5,
                          -FRAME_Y_RADIUS + margin_bot + box.get_height() * 0.5, 0]))

    scene.play(Write(text_obj, run_time=0))
    scene.play(DrawBorderThenFill(box, stroke_width=DEFAULT_STROKE_WIDTH))


def my_title(text, **kwargs):
    text_obj = TextMobject(text, **kwargs)
    text_obj.to_edge(UP)
    underline = Line(LEFT, RIGHT)
    underline.next_to(text_obj, DOWN, buff=MED_SMALL_BUFF)
    underline.set_width(FRAME_WIDTH - 2)

    text_obj.add(underline)
    text_obj.underline = underline
    return text_obj


def get_move_group_animation(group, vector):
    animations = [MoveAlongPath(elem, ParametricFunction(
        lambda t: t * vector + np.array([elem.get_x(), elem.get_y(), elem.get_z()])))
                  for elem in group.submobjects]
    return animations


def get_coords(mobject: Mobject):
    return np.array([mobject.get_x(), mobject.get_y(), mobject.get_z()])


def line_up_text_mobjects(*text_mobjects: TextMobject, distance=1):
    fixed = 'acemnorsuvwxz'
    bottom_fixed = 'abcdefhiklmnorstuvwxz'
    descender_fixed = 'gpqyj'
    mid_fixed = ['+', '-', '=', '(', ')', '\\cdot']

    fixed_height = TextMobject('a').get_height()
    descender_level = fixed_height - TextMobject('g').get_height()
    cap_height = TextMobject('A').get_height()

    for text_mobject in text_mobjects:
        tex_string = text_mobject.get_tex_string()
        if tex_string[0] in bottom_fixed:
            text_mobject.shift(UP * (0 - text_mobject.get_bottom()[1]))
        if tex_string[0] in descender_fixed:
            text_mobject.shift(UP * (descender_level - text_mobject.get_bottom()[1]))
        if tex_string[0] in mid_fixed:
            text_mobject.set_y(fixed_height * 0.5)
        if tex_string[0].isupper():
            text_mobject.shift(UP * (cap_height - text_mobject.get_top()[1]))
        if tex_string[0] == '\\':
            raise Exception('not implemented')

    right_edge = 0
    for i, m in enumerate(text_mobjects):
        m.shift(RIGHT * (right_edge + m.get_width() * 0.5 + distance))
        right_edge += m.get_width() + distance

    return Group(*text_mobjects)

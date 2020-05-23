import numpy
from manimlib.animation.movement import MoveAlongPath
from manimlib.imports import *
from manimlib.mobject.functions import ParametricFunction


def text_fit_to_box(text, box: Rectangle):
    lines_n = len(text.split('\\\\'))
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
    group_center = group.get_center()
    animation = MoveAlongPath(group, ParametricFunction(
        lambda t: t * vector + group_center))

    return animation


def get_coords(mobject: Mobject):
    return np.array([mobject.get_x(), mobject.get_y(), mobject.get_z()])


def make_screen_frame(scene, **kwargs):
    screen_frame = Rectangle()
    screen_frame.stretch_to_fit_width(FRAME_WIDTH)
    screen_frame.stretch_to_fit_height(FRAME_HEIGHT)
    screen_frame.set_stroke(width=DEFAULT_STROKE_WIDTH)
    if isinstance(scene, SpecialThreeDScene):
        scene.add_fixed_orientation_mobjects(screen_frame)
    else:
        scene.add(screen_frame)


drawing_defaults = {
    'stroke_color': DARK_BLUE,
    'stroke_width': DEFAULT_STROKE_WIDTH / 2,
    'fill_opacity': 0.75
}


class Pyramid(VGroup):
    CONFIG = {
        "fill_opacity": 0.75,
        "fill_color": BLUE,
        "stroke_width": DEFAULT_STROKE_WIDTH,
        "side_length": 2,
    }

    def __init__(self, n=4, **kwargs):
        digest_config(self, kwargs)
        self.base_vertices_n = n
        self.outer_radius = self.side_length / (2 * math.sin(PI / n))
        self.height = self.side_length
        super().__init__(**kwargs)

    def generate_points(self):
        # base = RegularPolygon(self.base_vertices_n, shade_in_3d=True)
        start_vect = RIGHT * self.outer_radius
        vertices = compass_directions(self.base_vertices_n, start_vect)
        base = Polygon(*vertices, shade_in_3d=True)
        base.rotate(PI / 2, X_AXIS)
        self.add(base)
        top = np.array([0, self.height, 0])
        base_points = base.get_vertices().tolist()
        for i, v in enumerate(base_points):
            self.add((Polygon(v, base_points[(i + 1) % self.base_vertices_n], top, shade_in_3d=True)))


def get_onto_center_should(what, onto_what):
    center_should = onto_what.get_center() + UP * onto_what.get_height() / 2 + UP * what.get_height() / 2
    return center_should


def put_onto_animation(what, center_should):
    dif_vec = center_should - what.get_center()
    mid_point = what.get_center() + dif_vec * 0.5 + UP * dif_vec[1] * 2
    return MoveAlongPath(what, ParametricFunction(bezier([what.get_center(), mid_point, center_should])))


def move_to_border_and_scale_animation(group, direction, scale_factor):
    return AnimationGroup(ScaleInPlace(group, scale_factor),
                          get_move_group_animation(group,
                                                   group.copy().scale(scale_factor).align_on_border(
                                                       direction).get_center() - group.get_center()))


space_width = 0.2515478499999987

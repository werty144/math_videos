import numpy
from manimlib.animation.movement import MoveAlongPath
from manimlib.imports import *
from manimlib.mobject.functions import ParametricFunction


def text_fit_to_box(text, box: Rectangle):
    lines_n = len(text.split('\\\\'))
    text_obj = TextMobject(text, height=lines_n * 0.4)
    text_obj.set_color_by_tex(text, BLACK)
    box.stretch_to_fit_width(text_obj.get_width() + 0.2)
    box.stretch_to_fit_height(text_obj.get_height() + 0.4)
    text_obj.center()
    box.center()
    return text_obj


def draw_reference(scene: Scene, text):
    box = Rectangle()
    box.set_stroke(width=DEFAULT_STROKE_WIDTH * 2, color="#2f4f4f").set_fill(color=WHITE, opacity=1)
    text_obj = text_fit_to_box(text, box)
    leg = Rectangle().stretch_to_fit_width(0.3).stretch_to_fit_height(1).set_fill(color="#a0522d", opacity=1). \
        set_stroke(width=0)
    group = Group(box, text_obj)
    group.align_on_border(DR)
    leg.shift(box.get_bottom() - leg.get_top())
    scene.bring_to_back(box)
    group = Group(box, text_obj, leg)

    scene.play(FadeInFromDown(group))
    scene.wait(3)
    scene.play(FadeOutAndShiftDown(group))


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


def move_to_border_and_scale_animation(group, direction, scale_factor=1):
    return AnimationGroup(ScaleInPlace(group, scale_factor),
                          get_move_group_animation(group,
                                                   group.copy().scale(scale_factor).align_on_border(
                                                       direction).get_center() - group.get_center()))


space_width = 0.2515478499999987


def overscribe_text(text_mobject, overrscript):
    over_text = TextMobject(overrscript)
    over_text.set_height(0.3)
    shift = text_mobject.get_top() - over_text.get_bottom() + UP * 0.15
    over_text.shift(shift)
    return over_text


def swap_variables_animation(v1_ind, v2_ind, text_mobject: TextMobject):
    v1 = text_mobject.submobjects[v1_ind]
    v2 = text_mobject.submobjects[v2_ind]
    v1_text = text_mobject.submobjects[v1_ind].get_tex_string()
    v2_text = text_mobject.submobjects[v2_ind].get_tex_string()
    new_text = [obj.get_tex_string() for obj in text_mobject.submobjects]
    new_text[v1_ind] = v2_text
    new_text[v2_ind] = v1_text
    new_text_mobject = TextMobject(*new_text, arg_separator='')
    new_text_mobject.shift(text_mobject.get_left() - new_text_mobject.get_left())
    new_v1_center = new_text_mobject.submobjects[v2_ind].get_center()
    new_v2_center = new_text_mobject.submobjects[v1_ind].get_center()
    v1_movement = MoveAlongPath(v1, ParametricFunction(
        lambda t: clockwise_path()(v1.get_center(), new_v1_center, t)))
    v2_movement = MoveAlongPath(v2, ParametricFunction(
        lambda t: clockwise_path()(v2.get_center(), new_v2_center, t)))
    return v1_movement, v2_movement


def update_indices_map(from_pos, to_pos, indices_map):
    if from_pos > to_pos:
        for key, value in indices_map.items():
            if to_pos <= value < from_pos:
                indices_map[key] += 1
            if value == from_pos:
                indices_map[key] = to_pos
    if from_pos < to_pos:
        for key, value in indices_map.items():
            if from_pos < value <= to_pos:
                indices_map[key] -= 1
            if value == from_pos:
                indices_map[key] = to_pos


def inverse_dict(my_dict):
    result_dict = {}
    for key, value in my_dict.items():
        result_dict[value] = key
    return result_dict


def move_brackets_animation(lbr_ind, rbr_ind, left_end, right_end, text_mobject):
    text = text_mobject.submobjects
    indices_map = {}
    for i in range(len(text)):
        indices_map[i] = i

    if lbr_ind > left_end:
        update_indices_map(lbr_ind, left_end, indices_map)
    else:
        update_indices_map(lbr_ind, left_end - 1, indices_map)

    new_rbr_ind = indices_map[rbr_ind]
    new_right_end = indices_map[right_end]
    if new_rbr_ind > new_right_end:
        update_indices_map(new_rbr_ind, new_right_end + 1, indices_map)
    else:
        update_indices_map(new_rbr_ind, new_right_end, indices_map)

    new_text = [text[inverse_dict(indices_map)[i]].get_tex_string() for i in range(len(text))]
    new_text_mobject = TextMobject(*new_text, arg_separator='')
    new_text_mobject.shift(text_mobject.get_left() - new_text_mobject.get_left())
    animations = [get_move_group_animation
                  (text[i], new_text_mobject.submobjects[indices_map[i]].get_center() - text[i].get_center())
                  for i in range(len(text))]
    return animations


def substitution_animation(var_ind, subst, text: TextMobject, scene):
    var = text.submobjects[var_ind]
    subst_text = TextMobject(subst)
    subst_text.set_color_by_tex_to_color_map({subst: var.get_color()})
    # subst_text.set_width(var.get_width())
    new_text = [obj.get_tex_string() for obj in text.submobjects]
    new_text[var_ind] = subst
    new_mobj = TextMobject(*new_text, arg_separator='')
    new_mobj.shift(text.get_left() - new_mobj.get_left())
    new_center = new_mobj.submobjects[var_ind].get_center()
    subst_text.shift(new_center - subst_text.get_center())
    text.submobjects[var_ind] = subst_text
    scene.remove(var)
    return FadeInFrom(subst_text, UP), FadeOutAndShiftDown(var)


def get_together_animation(group1, group2):
    diff = group2.get_left()[0] - group1.get_right()[0]
    return get_move_group_animation(group1, RIGHT * diff / 4), get_move_group_animation(group2, LEFT * diff / 4)


class My_bullet_list(Mobject):
    def __init__(self, n):
        Mobject.__init__(self)
        for _ in range(n):
            dot = TexMobject("\\cdot").scale(2)
            self.add(dot)
        dot_group = Group(*self.submobjects)
        dot_group.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=LARGE_BUFF
        )

    def fade_in_dot_animation(self, dot_ind):
        return FadeIn(self.submobjects[dot_ind])

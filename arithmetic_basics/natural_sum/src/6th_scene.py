from manimlib.imports import *
from src.functions import *


class Scene6(Scene):
    def construct(self):
        pow_func = TextMobject('$pow($', '$x$', ', ', '$y$', '$) =$', ' $x$', '$^y$', arg_separator='')
        pow_func.scale(1.5)
        pow_func.set_color_by_tex_to_color_map({'$x$': GREEN, '$y$': BLUE, '$^y$': BLUE})
        self.wait(2)
        self.play(FadeIn(pow_func))
        self.wait(1.5)
        self.play(move_to_border_and_scale_animation(pow_func, UP, 1), run_time=1.5)
        self.wait(1)

        # time passed 7

        new_middle_y = (pow_func.get_bottom()[1] - FRAME_Y_RADIUS) / 2

        pow_23 = TextMobject('$pow($', '$2$', ', ', '$3$', '$)$',  ' $=$ ', '$2$', '$^3$ ', '$=$ ', '8', arg_separator='')
        pow_23.set_color_by_tex_to_color_map({'$2$': GREEN, '$3$': BLUE, '$^3$': BLUE, '8': GREEN})
        pow_23.shift(UP * new_middle_y)
        self.play(FadeIn(Group(*pow_23.submobjects[:5]), run_time=1.5))
        self.wait(0.5)
        self.play(FadeIn(Group(*pow_23.submobjects[5:8]), run_time=1.5))
        self.wait(0.5)
        self.play(FadeIn(Group(*pow_23.submobjects[8:10]), run_time=1.5))
        self.wait(0.5)

        neq = TextMobject('$\\neq$')
        neq.shift(UP * new_middle_y)
        neq.set_color_by_tex('$\\neq$', RED)

        pow_23_shift = neq.get_left() - pow_23.get_right() + LEFT * space_width
        self.play(get_move_group_animation(pow_23, pow_23_shift), run_time=1.5)
        self.wait(0.5)

        # time passed 15

        self.wait(1)

        pow_32 = TextMobject('9', ' $=$ ', '$3$', '$^2$', ' $=$ ', '$pow($', '$3$', ', ', '$2$', '$)$', arg_separator='')
        pow_32.set_color_by_tex_to_color_map({'$2$': GREEN, '$3$': BLUE, '$^2$': GREEN, '9': BLUE})
        pow_32.shift(UP * new_middle_y)
        pow_32_shift = neq.get_right() - pow_32.get_left() + RIGHT * space_width
        pow_32.shift(pow_32_shift)
        self.play(FadeIn(Group(*pow_32.submobjects[5:10]), run_time=1.5))
        self.wait(0.5)
        self.play(FadeIn(Group(*pow_32.submobjects[2:5]), run_time=1.5))
        self.wait(0.5)
        self.play(FadeIn(Group(*pow_32.submobjects[0:2], run_time=1.5)))
        self.wait(0.5)
        self.play(FadeIn(neq))

        # time passed 23

        pow_32_func = Group(
            *pow_32.submobjects[5:]
        ).copy()
        self.add(pow_32_func)
        self.remove(
            *pow_32.submobjects[5:]
        )
        pow_23_func = Group(
            *pow_23.submobjects[:5]
        ).copy()
        self.add(pow_23_func)
        self.remove(
            *pow_23.submobjects[:5]
        )

        left_shift = neq.get_left() - pow_23_func.get_right() + LEFT * space_width
        right_shift = neq.get_right() - pow_32_func.get_left() + RIGHT * space_width
        self.play(get_move_group_animation(pow_23_func, left_shift),
                  get_move_group_animation(pow_32_func, right_shift),
                  FadeOut(Group(*pow_23.submobjects[5:])),
                  FadeOut(Group(*pow_32.submobjects[:5])),
                  run_time=2
                  )
        self.wait(2)

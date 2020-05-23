from manimlib.imports import *
from src.functions import *


class Scene6(Scene):
    def construct(self):
        make_screen_frame(self)
        pow_func = TextMobject('$pow($', '$x$', ', ', '$y$', '$) =$', ' $x$', '$^y$', arg_separator='')
        pow_func.scale(1.5)
        pow_func.set_color_by_tex_to_color_map({'$x$': GREEN, '$y$': BLUE, '$^y$': BLUE})
        self.play(Write(pow_func))
        self.play(move_to_border_and_scale_animation(pow_func, UP, 1))
        pow_23 = TextMobject('$pow($', '$2$', ', ', '$3$', '$)$',  ' $=$ ', '$2$', '$^3$ ', '$=$ ', '8', arg_separator='')
        pow_23.set_color_by_tex_to_color_map({'$2$': GREEN, '$3$': BLUE, '$^3$': BLUE, '8': GREEN})
        self.play(Write(pow_23))

        neq = TextMobject('$\\neq$')
        neq.set_color_by_tex('$\\neq$', RED)

        pow_23_shift = neq.get_left() - pow_23.get_right() + LEFT * space_width
        self.play(get_move_group_animation(pow_23, pow_23_shift))

        pow_32 = TextMobject('9', ' $=$ ', '$3$', '$^2$', ' $=$ ', '$pow($', '$3$', ', ', '$2$', '$)$', arg_separator='')
        pow_32.set_color_by_tex_to_color_map({'$2$': GREEN, '$3$': BLUE, '$^2$': GREEN, '9': BLUE})
        pow_32_shift = neq.get_right() - pow_32.get_left() + RIGHT * space_width
        pow_32.shift(pow_32_shift)
        self.play(Write(pow_32))
        self.play(FadeIn(neq))
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
                  FadeOut(Group(*pow_32.submobjects[:5]))
                  )
        self.wait()

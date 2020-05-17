from manimlib.imports import *

from src.functions import draw_reference, my_title


class Intro(Scene):
    def construct(self):
        title = my_title('Натуральные числа', color=BLUE, height=1)
        self.play(Write(title))
        self.wait(3)
        some_numbers = [TextMobject(f'{i}', height=0.7) for i in range(1, 11)]
        ldots = TextMobject('$$11 \\ldots$$', height=0.7)
        some_numbers[0].shift(LEFT * 6)
        for i, number in enumerate(some_numbers):
            if i >= 1:
                number.next_to(some_numbers[i - 1], RIGHT * 2)
        ldots.next_to(some_numbers[-1], RIGHT * 2)
        some_numbers.append(ldots)
        numbers_group = Group(*some_numbers)
        numbers_group.center()
        self.play(FadeIn(numbers_group, lag_ratio=0.1, run_time=3, rate_func=linear))
        self.wait(3)
        draw_reference(self, 'В математике\\\\\n'
                             'множество натуральных чисел\\\\\n'
                             'принято обозначать\\\\\n'
                             '~\\\\\n'
                             '{\\Huge $\\mathbb{N}$}')
        self.wait(1)

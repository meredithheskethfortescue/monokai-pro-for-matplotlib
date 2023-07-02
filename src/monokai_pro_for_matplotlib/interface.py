from typing import Tuple


class Color(str):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self._value_rgb = None

    @property
    def as_rgb(self) -> Tuple[int, int, int]:
        # calculate rgb value just in time
        if '_value_rgb' not in self.__dict__:
            # strip leading '#' if present
            value = self.value.lstrip('#')
            # convert hex to rgb and save it for later in order to skip recomputation
            self._value_rgb = tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))

        return self._value_rgb


class Theme:
    def __init__(self, bg_light: str, bg_dark: str, bg_highlight: str, white: str, comment_gray: str, light_gray: str,
                 gray: str, red: str, orange: str, yellow: str, green: str, blue: str, purple: str):
        self._bg_light = Color(bg_light)
        self._bg_dark = Color(bg_dark)
        self._bg_highlight = Color(bg_highlight)

        self._white = Color(white)
        self._comment_gray = Color(comment_gray)  # comments
        self._light_gray = Color(light_gray)  # self
        self._gray = Color(gray)  # parentheses, dots, commas
        self._red = Color(red)

        self._orange = Color(orange)
        self._yellow = Color(yellow)
        self._green = Color(green)
        self._blue = Color(blue)
        self._purple = Color(purple)

    @property
    def bg_light(self) -> Color:
        return self._bg_light

    @bg_light.setter
    def bg_light(self, value: str):
        self._bg_light = Color(value)

    @property
    def bg_dark(self) -> Color:
        return self._bg_dark

    @bg_dark.setter
    def bg_dark(self, value: str):
        self._bg_dark = Color(value)

    @property
    def bg_highlight(self) -> Color:
        return self._bg_highlight

    @bg_highlight.setter
    def bg_highlight(self, value: str):
        self._bg_highlight = Color(value)

    @property
    def white(self) -> Color:
        return self._white

    @white.setter
    def white(self, value: str):
        self._white = Color(value)

    @property
    def comment_gray(self) -> Color:
        return self._comment_gray

    @comment_gray.setter
    def comment_gray(self, value: str):
        self._comment_gray = Color(value)

    @property
    def light_gray(self) -> Color:
        return self._light_gray

    @light_gray.setter
    def light_gray(self, value: str):
        self._light_gray = Color(value)

    @property
    def gray(self) -> Color:
        return self._gray

    @gray.setter
    def gray(self, value: str):
        self._gray = Color(value)

    @property
    def red(self) -> Color:
        return self._red

    @red.setter
    def red(self, value: str):
        self._red = Color(value)

    @property
    def orange(self) -> Color:
        return self._orange

    @orange.setter
    def orange(self, value: str):
        self._orange = Color(value)

    @property
    def yellow(self) -> Color:
        return self._yellow

    @yellow.setter
    def yellow(self, value: str):
        self._yellow = Color(value)

    @property
    def green(self) -> Color:
        return self._green

    @green.setter
    def green(self, value: str):
        self._green = Color(value)

    @property
    def blue(self) -> Color:
        return self._blue

    @blue.setter
    def blue(self, value: str):
        self._blue = Color(value)

    @property
    def purple(self) -> Color:
        return self._purple

    @purple.setter
    def purple(self, value: str):
        self._purple = Color(value)

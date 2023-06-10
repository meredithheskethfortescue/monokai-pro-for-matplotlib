"""
todo: Palette.green.as_rgb()
"""
import abc
from dataclasses import dataclass


class ThemeInterface(abc.ABCMeta):
    bg_light: str
    bg_dark: str
    bg_highlight: str

    white: str
    comment_gray: str
    light_gray: str
    gray: str

    red: str
    orange: str
    yellow: str
    green: str
    blue: str
    purple: str


@dataclass
class Classic(metaclass=ThemeInterface):
    """Classic Monokai Theme"""
    bg_light = '272822'
    bg_dark = '1d1e19'
    bg_highlight = '31322c'

    white = 'fdfff0'
    comment_gray = '6e7065'
    light_gray = 'c0c1b4'
    gray = '919287'

    red = 'ff0073'
    orange = 'ff9100'
    yellow = 'e7dc66'
    green = '97e600'
    blue = '3bdcf1'
    purple = 'b67aff'


@dataclass
class Machine(metaclass=ThemeInterface):
    """Monokai Pro - Filter: Machine"""
    bg_light = '273136'
    bg_dark = '1d2528'
    bg_highlight = '313a3e'

    white = 'f0fffc'
    comment_gray = '697678'  # comments
    light_gray = 'b6c5c3'  # self
    gray = '889797'  # parentheses, dots, commas

    red = 'FF6D7E'
    orange = 'FFB270'
    yellow = 'FFED72'
    green = 'A2E57B'
    blue = '7CD5F1'
    purple = 'BAA0F8'


class Octagon(metaclass=ThemeInterface):
    """Monokai Pro - Filter: Octagon"""
    bg_light = '282a3b'
    bg_dark = '181924'
    bg_highlight = '313444'

    white = 'e9f2f1'
    comment_gray = '696d78'  # comments
    light_gray = 'b1b9bd'  # self
    gray = '878d95'  # parentheses, dots, commas

    red = 'ff5379'
    orange = 'ff9554'
    yellow = 'ffd65d'
    green = 'b3da50'
    blue = '90d4ba'
    purple = 'c997cc'


@dataclass
class Ristretto(metaclass=ThemeInterface):
    """Monokai Pro - Filter: Ristretto"""
    bg_light = '2d2525'
    bg_dark = '221c1c'
    bg_highlight = '372f2f'

    white = 'fff0f3'
    comment_gray = '73696a'  # comments
    light_gray = 'c5b6b8'  # self
    gray = '96898b'  # parentheses, dots, commas

    red = '96898b'
    orange = 'ff866b'
    yellow = 'ffcb5e'
    green = 'a2dd6d'
    blue = '6eddcc'
    purple = 'a9a7ef'


@dataclass
class Spectrum(metaclass=ThemeInterface):
    """Monokai Pro - Filter: Spectrum"""
    bg_light = '222222'
    bg_dark = '191919'
    bg_highlight = '2c2c2d'

    white = 'f8f0ff'
    comment_gray = '69676c'  # comments
    light_gray = 'bbb6c1'  # self
    gray = 'bbb6c1'  # parentheses, dots, commas

    red = 'ff4e8e'
    orange = 'ff8c48'
    yellow = 'fee551'
    green = '5edc89'
    blue = '1ed7e8'
    purple = '9787e8'

from dataclasses import dataclass


@dataclass
class Theme:
    # background colors
    bg_light: str
    bg_dark: str
    bg_highlight: str

    # text
    white: str
    comment_gray: str  # comments
    light_gray: str  # `self`
    gray: str  # parentheses, dots, commas

    # highlighting
    red: str
    orange: str
    yellow: str
    green: str
    blue: str
    purple: str


# Classic Monokai Theme
classic = Theme(
    bg_light='#272822',
    bg_dark='#1d1e19',
    bg_highlight='#31322c',
    white='#fdfff0',
    comment_gray='#6e7065',
    light_gray='#c0c1b4',
    gray='#919287',
    red='#ff0073',
    orange='#ff9100',
    yellow='#e7dc66',
    green='#97e600',
    blue='#3bdcf1',
    purple='#b67aff'
)

# Monokai Pro - Filter: Machine
machine = Theme(
    bg_light='#273136',
    bg_dark='#1d2528',
    bg_highlight='#313a3e',
    white='#f0fffc',
    comment_gray='#697678',
    light_gray='#b6c5c3',
    gray='#889797',
    red='#FF6D7E',
    orange='#FFB270',
    yellow='#FFED72',
    green='#A2E57B',
    blue='#7CD5F1',
    purple='#BAA0F8'
)

# Monokai Pro - Filter: Octagon
octagon = Theme(
    bg_light='#282a3b',
    bg_dark='#181924',
    bg_highlight='#313444',
    white='#e9f2f1',
    comment_gray='#696d78',
    light_gray='#b1b9bd',
    gray='#878d95',
    red='#ff5379',
    orange='#ff9554',
    yellow='#ffd65d',
    green='#b3da50',
    blue='#90d4ba',
    purple='#c997cc'
)

# Monokai Pro - Filter: Ristretto
ristretto = Theme(
    bg_light='#2d2525',
    bg_dark='#221c1c',
    bg_highlight='#372f2f',
    white='#fff0f3',
    comment_gray='#73696a',
    light_gray='#c5b6b8',
    gray='#96898b',
    red='#96898b',
    orange='#ff866b',
    yellow='#ffcb5e',
    green='#a2dd6d',
    blue='#6eddcc',
    purple='#a9a7ef'
)

# Monokai Pro - Filter: Spectrum
spectrum = Theme(
    bg_light='#222222',
    bg_dark='#191919',
    bg_highlight='#2c2c2d',
    white='#f8f0ff',
    comment_gray='#69676c',
    light_gray='#bbb6c1',
    gray='#bbb6c1',
    red='#ff4e8e',
    orange='#ff8c48',
    yellow='#fee551',
    green='#5edc89',
    blue='#1ed7e8',
    purple='#9787e8'
)

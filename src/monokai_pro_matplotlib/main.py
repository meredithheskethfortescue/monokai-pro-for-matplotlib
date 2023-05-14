"""Monokai Pro for Matplotlib"""
import os

import matplotlib.pyplot as plt


class Palette:
    # todo: Palette.green.as_rgb()
    # todo: other filter
    # Filter: Machine
    bg_light = '273136'  # rgb(39, 49, 54)
    bg_dark = '1d2528'  # rgb(29, 37, 40)
    bg_highlight = '313a3e'  # rgb(49 58 62)
    white = 'f0fffc'  # rgb(240 255 252)
    comment_gray = '94a2a2'  # rgb(148 162 162)
    gray = '8b9798'  # rgb(139, 151, 152)
    red = 'FF6D7E'  # rgb(255, 109, 126)
    orange = 'FFB270'  # rgb(255, 178, 112)
    yellow = 'FFED72'  # rgb(255, 237, 114)
    green = 'A2E57B'  # rgb(162, 229, 123)
    blue = '7CD5F1'  # rgb(124, 213, 241)
    purple = 'BAA0F8'  # rgb(186, 160, 248)


def overwrite_current_settings():
    # set parameter
    plt.rcParams['axes.facecolor'] = Palette.bg_light
    plt.rcParams['figure.facecolor'] = Palette.bg_dark
    plt.rcParams['axes.edgecolor'] = Palette.white
    plt.rcParams['xtick.color'] = Palette.white
    plt.rcParams['ytick.color'] = Palette.white
    plt.rcParams['axes.titlecolor'] = Palette.white
    plt.rcParams['legend.labelcolor'] = Palette.white
    plt.rcParams['grid.color'] = Palette.white

    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        Palette.blue,
        Palette.orange,
        Palette.green,
        Palette.red,
        Palette.purple,
        Palette.gray,
        Palette.yellow,
    ])


def create_mplstyle_from_template(palette: Palette, path: str):
    # read template
    with open('template_monokai.css', 'r') as file_template:
        template = file_template.read()

    # fill template
    # todo: add header to outputfile
    style_sheet = template.format(**Palette.__dict__)

    # write out
    dir_out = os.path.dirname(path)
    if dir_out:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+') as file_out:
        file_out.write(style_sheet)


if __name__ == '__main__':
    # overwrite_current_settings()
    create_mplstyle_from_template(Palette(), 'machine.mplstyle')

    def main():
        # get list of available parameters and their current value
        # for key, value in zip(plt.rcParams, plt.rcParams.values()):
        #     print(f"{key} : {value}")

        plt.style.use('./machine.mplstyle')

        # test plot
        plt.figure()
        for it in range(7):
            plt.plot([0, it], '-o', label=f"$n_{it} = {it}$ lorem ipsum")

        plt.title("Title")
        plt.grid()
        plt.legend()
        plt.show()


    main()

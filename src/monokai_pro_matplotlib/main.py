"""Monokai Pro for Matplotlib"""
import os

import matplotlib.pyplot as plt

import palette


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


def create_mplstyle_from_template(palette, path: str):
    # read template
    with open('template.mplstyle', 'r') as file_template:
        template = file_template.read()

    # fill template
    # todo: add header to outputfile
    style_sheet = template.format(**palette.__dict__)

    # write out
    dir_out = os.path.dirname(path)
    if dir_out:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+') as file_out:
        file_out.write(style_sheet)


if __name__ == '__main__':
    # overwrite_current_settings()
    create_mplstyle_from_template(palette.Machine, 'machine.mplstyle')


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

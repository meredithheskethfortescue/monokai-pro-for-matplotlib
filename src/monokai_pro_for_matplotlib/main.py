"""Monokai Pro for Matplotlib"""
import os

import matplotlib.pyplot as plt

import themes


def create_mplstyle_from_template(theme: themes.ThemeInterface, dir_out: str = './monokai-pro/'):
    """Create a *.mplstyle file from template"""
    # read template
    with open('template.mplstyle', 'r') as file_template:
        template = file_template.read()

    # fill template
    style_sheet = template.format(**theme.__dict__, theme_filter=theme.__name__)

    # make sure that the output directory exists
    os.makedirs(os.path.dirname(dir_out), exist_ok=True)
    # name output file after the filter (which is also the class name but use the lower case here)
    path_out = os.path.join(dir_out, f'{theme.__name__.lower()}.mplstyle')
    # write out
    with open(path_out, 'w+') as file_out:
        file_out.write(style_sheet)


def main():
    """Generate *.mplstyle files from template"""
    create_mplstyle_from_template(themes.Classic)
    create_mplstyle_from_template(themes.Machine)
    create_mplstyle_from_template(themes.Octagon)
    create_mplstyle_from_template(themes.Ristretto)
    create_mplstyle_from_template(themes.Spectrum)


def run_example():
    # use one of the newly created themes
    plt.style.use('./monokai-pro/machine.mplstyle')

    # get list of available parameters and their current value
    for key, value in zip(plt.rcParams, plt.rcParams.values()):
        print(f"{key} : {value}")

    # test plot
    for it in range(7):
        plt.plot([0, it], '-o', label=rf"$n_{it} = {it}\,\sigma$ label")

    plt.text(.5, 5, "text")
    plt.title("Title")
    plt.xlabel("$x$ label")
    plt.ylabel("$y$ label")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
    run_example()

"""Create Monokai Pro stylesheets from templates
Run this to recreate the *.mplstyle files for the Monokai Pro theme from the dataclasses.
"""
import os

import matplotlib.pyplot as plt

import themes


def create_mplstyle_from_template(theme: themes.Theme, path_out: str, description: str):
    """Create a *.mplstyle file from template"""
    # read template
    with open('template.mplstyle', 'r') as file_template:
        template = file_template.read()

    # strip the leading `#` from the strings
    theme_without_hashes = {key: value[1:] for key, value in theme.__dict__.items()}
    # fill the template
    style_sheet = template.format(**theme_without_hashes,
                                  theme_filter=description)

    # split the path into dir and filename
    dir_out, filename = os.path.split(path_out)
    # make sure that the output directory exists
    os.makedirs(os.path.dirname(dir_out), exist_ok=True)
    # name output file after the filter (which is also the class name but use the lower case here)
    # strip the leading # from the string
    path_out = os.path.join(dir_out, f'{filename.lower()}.mplstyle')
    # write out
    with open(path_out, 'w+') as file_out:
        file_out.write(style_sheet)


def create_monokai_stylesheets():
    """Generate *.mplstyle files from template"""
    create_mplstyle_from_template(themes.classic, './monokai-pro/classic', "Monokai Theme (Classic)")
    create_mplstyle_from_template(themes.machine, './monokai-pro/machine', "Monokai Pro Theme - Filter: Machine")
    create_mplstyle_from_template(themes.octagon, './monokai-pro/octagon', "Monokai Pro Theme - Filter: Octagon")
    create_mplstyle_from_template(themes.ristretto, './monokai-pro/ristretto', "Monokai Pro Theme - Filter: Ristretto")
    create_mplstyle_from_template(themes.spectrum, './monokai-pro/spectrum', "Monokai Pro Theme - Filter: Spectrum")


def run_example():
    # use one of the newly created themes
    plt.style.use('./monokai-pro/machine.mplstyle')

    # get a list of the available parameters and their current value
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
    create_monokai_stylesheets()
    run_example()

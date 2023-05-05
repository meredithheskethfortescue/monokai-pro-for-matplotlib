"""Monokai Pro for Matplotlib"""
import matplotlib.pyplot as plt

# palette
color_base_bg_light = '#273136'  # rgb(39, 49, 54)
color_base_bg_dark = '#1d2528'  # rgb(29, 37, 40)
color_text_white = '#8b9798'

color_gray = '#8b9798'  # rgb(139, 151, 152) todo: find correct comment color

color_red = '#FF6D7E'  # rgb(255, 109, 126)
color_orange = '#FFB270'  # rgb(255, 178, 112)
color_yellow = '#FFED72'  # rgb(255, 237, 114)
color_green = '#A2E57B'  # rgb(162, 229, 123)
color_blue = '#7CD5F1'  # rgb(124, 213, 241)
color_purple = '#BAA0F8'  # rgb(186, 160, 248)

# set parameter
plt.rcParams['axes.facecolor'] = color_base_bg_light
plt.rcParams['figure.facecolor'] = color_base_bg_dark
plt.rcParams['axes.edgecolor'] = color_text_white
plt.rcParams['xtick.color'] = color_text_white
plt.rcParams['ytick.color'] = color_text_white
plt.rcParams['axes.titlecolor'] = color_text_white
plt.rcParams['legend.labelcolor'] = color_text_white
plt.rcParams['grid.color'] = color_gray

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
    color_blue,
    color_orange,
    color_green,
    color_red,
    color_purple,
    color_gray,
    color_yellow,
])

if __name__ == '__main__':
    def main():
        # get list of available parameters and their current value
        for key, value in zip(plt.rcParams, plt.rcParams.values()):
            print(f"{key} : {value}")

        # test plot
        plt.figure()
        for it in range(7):
            plt.plot([0, it], '-o', label=f"$n_{it} = {it}$ lorem ipsum")

        plt.title("Title")
        plt.grid()
        plt.legend()
        plt.show()


    main()

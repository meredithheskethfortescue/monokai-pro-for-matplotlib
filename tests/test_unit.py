import unittest

import matplotlib.pyplot as plt

import monokai_pro_for_matplotlib as monokai


class TestPackage(unittest.TestCase):
    def test_import(self):
        # noinspection PyUnresolvedReferences
        from monokai_pro_for_matplotlib import classic as theme
        # noinspection PyUnresolvedReferences
        from monokai_pro_for_matplotlib import machine
        # noinspection PyUnresolvedReferences
        from monokai_pro_for_matplotlib import octagon
        # noinspection PyUnresolvedReferences
        from monokai_pro_for_matplotlib import ristretto
        # noinspection PyUnresolvedReferences
        from monokai_pro_for_matplotlib import spectrum

        __ = theme.green

        import monokai_pro_for_matplotlib as monokai
        __ = monokai.machine
        __ = monokai.machine.green

    def test_use_stylesheet(self):
        plt.style.use('../src/monokai_pro_for_matplotlib/monokai-pro/classic.mplstyle')
        plt.style.use('../src/monokai_pro_for_matplotlib/monokai-pro/machine.mplstyle')
        plt.style.use('../src/monokai_pro_for_matplotlib/monokai-pro/octagon.mplstyle')
        plt.style.use('../src/monokai_pro_for_matplotlib/monokai-pro/ristretto.mplstyle')
        plt.style.use('../src/monokai_pro_for_matplotlib/monokai-pro/spectrum.mplstyle')

    @unittest.skip("Installation of stylesheets, known to matplotlib not implemented yet")
    def test_use_installed_style(self):
        plt.style.use('monokai-pro/classic')
        plt.style.use('monokai-pro/machine')
        plt.style.use('monokai-pro/octagon')
        plt.style.use('monokai-pro/ristretto')
        plt.style.use('monokai-pro/spectrum')

    def test_colors_hex(self):
        theme = monokai.machine
        self.assertEqual('a2e57B'.casefold(), theme.green.casefold())

    @unittest.skip("`as_rgb` feature is not implemented yet")
    def test_colors_rgb(self):
        theme = monokai.machine
        self.assertEqual('a2e57B'.casefold(), theme.green.as_rgb)

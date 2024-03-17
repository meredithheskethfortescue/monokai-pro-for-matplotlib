import unittest

import matplotlib.pyplot as plt

from monokai_pro_for_matplotlib.themes import machine as theme


class TestThemeClasses(unittest.TestCase):
    def test_use_with_matplotlib(self):
        """Use the value from a theme class to ensure that it can be used directly in matplotlib"""
        plt.plot([0, 1, 2], color=theme.green)

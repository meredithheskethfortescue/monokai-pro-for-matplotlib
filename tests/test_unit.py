import unittest


class TestUnit(unittest.TestCase):
    def test_hex2rgb(self):
        from src.monokai_pro_for_matplotlib import themes

        theme = themes.Machine

        print(f"#{theme.green} = rgb{theme.green.as_rgb}")

    def test_color_jit_conversion(self):
        from monokai_pro_for_matplotlib.themes import Machine as theme

        self.assertEqual((162, 229, 123), theme.green.as_rgb)

        theme.green = 'ff0000'
        self.assertEqual((255, 0, 0), theme.green.as_rgb)

# Monokai for Matplotlib

## Quickstart

The most simplest way to use this theme is to make matplotlib use the stylesheet:

```python
import matplotlib.pyplot as plt

plt.style.use('monokai-pro/machine')
```

The available filters are:

- 'monokai-pro/machine'
- 'monokai-pro/octagon'
- 'monokai-pro/ristretto'
- 'monokai-pro/spectrum'
- 'monokai-pro/classic'

## Using specific colors

If you want to set some colors explicitly, you can import this package:

```python
import matplotlib.pyplot as plt
import monokai_pro_for_matplotlib.Machine as theme

# use a specific color of the imported theme
plt.plot([0, 0], [1, 1], '-o', color=theme.green)
plt.show()
```

Additionally you can use the provided interface to get code completion without specifying the exact filter.

```python
import monokai_pro_for_matplotlib.interface
import matplotlib.pyplot as plt
import monokai_pro_for_matplotlib as monokai


def example_using_interface(
        theme: monokai_pro_for_matplotlib.interface.ThemeInterface):  # type hint the theme as of the monokai family
    plt.plot([0, 0], [1, 1], '-o', color=theme.green)  # use a specific color of the given theme
    plt.show()


if __name__ == '__main__':
    example_using_interface(monokai.Machine)
```

The colors are formatted as hex-code string (without a leading '#').
If you need it formatted as rgb you can get it as such:
```python
from src.monokai_pro_for_matplotlib import themes
# choose a theme
theme = themes.Machine
# print hex and rgb representation
print(f"#{theme.green} = rgb{theme.green.as_rgb}")
# -> #A2E57B = rgb(162, 229, 123)
```

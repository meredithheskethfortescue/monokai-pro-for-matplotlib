from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='monokai-pro-for-matplotlib',
    version='0.0.1',
    author="Raphael Stascheit",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[req for req in requirements if req[:2] != "# "],
    packages=['monokai-pro-for-matplotlib'],
    package_data={'monokai-pro': ['machine.mplstyle',
                                  'octagon.mplstyle',
                                  'ristretto.mplstyle',
                                  'spectrum.mplstyle',
                                  'classic.mplstyle']},  # plt.style.use('monokai-pro/machine')
)

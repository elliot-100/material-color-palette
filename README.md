# material-2014-colors

Google's original [2014 Material Design color palettes](https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors)
as a Python library package.

Because I wanted to use the palettes in some of my projects, but didn't want to
copy-paste values, and couldn't find an existing implementation that was simple
and complete.

Fully type-hinted and with a test suite.

## Installation

Not yet available on PyPI, so install from GitHub, e.g.:

```sh
pip install git+https://github.com/elliot-100/material-2014-colors
```

I recommend installing a specific version, e.g.:

```sh
pip install git+https://github.com/elliot-100/material-2014-colors@v0.2.0
```

## Usage

```pycon
>>> from material_2014_colors import Color
>>> FOREGROUND = Color("red", 700)
>>> FOREGROUND
Color(name='red', shade=700, rgb=(211, 47, 47))

# Use RGB triplet representation in e.g. pygame/pygame-ce:
>>> FOREGROUND.rgb
(211, 47, 47)

# Use hex string representation in e.g. Matplotlib:
>>> FOREGROUND.hex
'#d32f2f'

# r, g, b properties should cover any other need:
>>> f"r={FOREGROUND.r/255}, g={FOREGROUND.g/255}, b={FOREGROUND.b/255}, a=1.0"
'r=0.8274509803921568, g=0.1843137254901961, b=0.1843137254901961, a=1.0'

# Accent colours use the original notation, so shade value is a string  
>>> COLOR_1 = Color("pink", "a100")

# You can use strings for non-accented colours too, if you want to be consistent
>>> COLOR_2 = Color("teal", "100")

# Useful, contextual error messages:
>>> COLOR_3 = Color("lime_green") 
Traceback (most recent call last):
...
ValueError: 'lime_green' isn't a valid Material color name. Allowed values: 'amber', 'black', 'blue', 'blue gray',
'blue_gray', 'brown', 'cyan', 'deep orange', 'deep purple', 'deep_orange', 'deep_purple', 'gray', 'green', 'indigo',
'light blue', 'light green', 'light_blue', 'light_green', 'lime', 'orange', 'pink', 'purple', 'red', 'teal', 'white',
'yellow'.

>>> COLOR_3 = Color("lime")
Traceback (most recent call last):
...
ValueError: Shade must be specified for Material color 'lime'.

>>> COLOR_3 = Color("yellow", 950)
Traceback (most recent call last):
...
ValueError: '950' isn't a valid shade for Material color 'yellow'. Allowed values: 50, 100, 200, 300, 400, 500, 600,
700, 800, 900, 'a100', 'a200', 'a400', 'a700'.

>>> COLOR_3 = Color("gray", 950)
Traceback (most recent call last):
...
ValueError: '950' isn't a valid shade for Material color 'gray'. Allowed values: 50, 100, 200, 300, 400, 500, 600, 700,
800, 900.
```

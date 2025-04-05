#!/usr/bin/env python3
# Phoenix Fractal Visualizer - a variation of the Julia Fractal

#               Copyright © DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it isn't allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macrame, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).

import sys
from palettes import grad
from pathlib import Path



# these ones are the ones that i'm using in this program
from tkinter import Tk, Canvas, PhotoImage, mainloop
import time


SIZE = 512


def getColorFromPalette(z, fc):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """

    # c = complex(0.5667, 0.0)
    c = complex(fc['creal'], fc['cimag'])
    # pheonix = complex(-0.5, 0.0)
    pheonix = complex(fc['preal'], fc['pimag'])
    zPrev = 0+0j
    for i in range(102):
        zSave = z
        z = z * z + c + (pheonix * zPrev)
        zPrev = zSave
        if abs(z) > 2:
            return grad[i]
    return grad[101]


def fractal_config(d, n):

    if n in d:
        return d[n]
    else:
        return None


Save_As_Picture = True
img = None


def show_status(rows):
    portion = (SIZE - rows) / SIZE
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return f'[{status_percent} {status_bar}]'


def paint_fractal(fractal, w, img):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    half_axis = fractal['axisLength'] / 2.0
    min_x = fractal['centerX'] - half_axis
    min_y = fractal['centerY'] - half_axis
    max_x = fractal['centerX'] + half_axis

    canvas = Canvas(window, width=SIZE, height=SIZE, bg='#000000')
    canvas.pack()
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")

    pixel_size = abs(max_x - min_x) / SIZE

    for row in range(SIZE, 0, -1):
        row_colors = []
        for col in range(SIZE):
            x = min_x + col * pixel_size
            y = min_y + row * pixel_size
            point = complex(x, y)
            color = getColorFromPalette(point, fractal)
            row_colors.append(color)

        if col == SIZE - 1:
            img.put('{' + ' '.join(row_colors) + '}', to=(0, SIZE - row))
            window.update()  # Refresh the window to display the current row.
            print(show_status(row), end='\r', file=sys.stderr)
            row_colors = []  # Reset for the next row.


fractal = {
        # The full Phoneix set
        'phoenix': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        # This one looks like a peacock's tail to me
        'peacock': {
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        # Two or more monkeys having a scuffle
        'monkey-knife-fight': {
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        # This one makes me hungry to look at
        'shrimp-cocktail': {
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },
        }


def cast_hash_map(fname):
    """
    Function p(f)
    Input: f
    Output: a tuple, or an exception (when it crashes)
    """

    f = open(fname)
    frac_centerx = None
    frac_centery = None
    frac_axislength = None
    frac_fname = fname
    frac_preal = 0.0
    frac_creal = .0

    frac_name = Path(fname)


    frac_type = "phoenix"

    n = 0
    for line in f:
        n +=1
        # n++;  # this doesn't work in Python version 3.13
        if line == '\n' or line.lstrip().startswith('#'):
            continue
        pair = line.strip().lower().replace(' ', '').split(':')
        if len(pair) != 2:
            raise RuntimeError(f"Parse error at line #{n} of {fname}: wrong number of tokens\n    {line}")
        if pair[0] == 'centerx':
            frac_centerx = float(pair[1])
        if pair[0] == 'centery':
            frac_centery = float(pair[1])
        if pair[0] == 'axislength':
            frac_axislength = float(pair[1])
        if pair[0] == 'type' and frac_type != pair[1]:
            print(f"{RED}Warning! incompatible fractal type detected: '{pair[1]}'{RST}", file=sys.stderr)
        if pair[0] == 'preal':
            frac['preal'] = float(pair[1])
        if pair[0] == 'creal':
            frac_creal = float(pair[1])
        if pair[0] == 'pimag':
            frac_pimag = float(pair[1])
        if pair[0] == 'cimag':
            frac_cimag = float(pair[1])

#
    f.close()

    if None in (frac_centerx, frac_centery, frac_axislength, frac_type):
        raise RuntimeError("A required parameter is missing")
    elif frac_axislength <= 0.00000000000000000000000000000000001:  # LOL, Python thinks this is zero!
        raise ValueError("axisLength must be positive")
    else:
        fname = dict()
        fname['name'] = frac_name
        fname['type'] = frac_type
        fname['centerX'] = frac_centerx
        fname['fname'] = frac_fname
        fname['pimag'] = frac_pimag

        fname['centerY'] = frac_centery
        fname['creal'] = frac_creal

        fname['preal'] = frac_preal
        fname['axisLength'] = frac_axislength

        fname['cimag'] = frac_cimag
        return (fname['name'], fname)


if __name__ == '__main__':
    """Main Mandelbrot Function"""
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        sys.exit(1)

    name,fractal = cast_hash_map(sys.argv[1])
    print("Rendering {} fractal".format(name), file=sys.stderr)
    before = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    paint_fractal(fractal, window, img)

    after = time.time()

    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{name}.png")
    print(f"Saved image to file {name}.png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

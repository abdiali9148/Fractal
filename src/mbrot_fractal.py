#!/usr/bin/env python3
# Mandelbrot Set Visualizer

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

from tkinter import Tk, Canvas, PhotoImage, mainloop
from pathlib import Path
import sys
import time
from palettes import palette

SIZE = 512  # the size of the image we will create is 512x512 pixels
MAX_ITERATIONS = 115


def show_status(rows, cols): # fine
    portion = (SIZE - rows) / SIZE
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return f'[{status_percent} {status_bar}]'


def compute_iteration(c, escape_radius=2):
    z = 0 + 0j
    for iteration in range(MAX_ITERATIONS):
        z = z * z + c
        if abs(z) > escape_radius:
            return iteration
    return MAX_ITERATIONS - 1


def get_color_from_palette(c, palette, escape_radius=2):
    z = 0 + 0j
    num_colors = len(palette)
    for iteration in range(num_colors):
        z = z * z + c
        if abs(z) > escape_radius:
            return palette[iteration]
    return palette[-1]


def pixel_color(c, palette, escape_radius=2):
    if palette is not None:
        return get_color_from_palette(c, palette, escape_radius)
    else:
        return compute_iteration(c, escape_radius)


def paint_fractal(fractal, window, img):

    half_axis = fractal['axisLen'] / 2.0
    minx = fractal['centerX'] - half_axis
    maxx = fractal['centerX'] + half_axis
    miny = fractal['centerY'] - half_axis

    # Create and display the canvas.
    canvas = Canvas(window, width=SIZE, height=SIZE, bg='#000000')
    canvas.pack()
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")

    pixel_size = abs(maxx - minx) / SIZE

    total_pixels = SIZE * SIZE
    row_colors = []

    for i in range(total_pixels):

        row = SIZE - (i // SIZE)
        col = i % SIZE

        x = minx + col * pixel_size
        y = miny + row * pixel_size
        point = complex(x, y)

        color = pixel_color(point, palette)
        row_colors.append(color)

        # When the end of a row is reached, update the image.
        if col == SIZE - 1:
            img.put('{' + ' '.join(row_colors) + '}', to=(0, SIZE - row))
            window.update()  # Refresh the window to display the current row.
            print(show_status(row, SIZE), end='\r', file=sys.stderr)
            row_colors = []  # Reset for the next row.


def cast_hash_map(fname):
    """
    Parses a mandelbrot data file into a dictionary
    returns a tuple of the form (DICT, FILENAME)
    """
    NAME = 'name'
    frac = {'fname': fname, NAME: Path(fname)}
    f = open(fname)
    for line in f:
        if line == '\n' or line.lstrip().startswith('#'):
            continue
        kv = line.replace(' ', '').rstrip().lower().split(":")
        if len(kv) != 2:
            error_msg = "Parse error at line #"
            raise RuntimeError(error_msg)
        key, value = kv
        if key == 'centerx':
            frac['centerX'] = float(value)
        if key == 'centery':
            frac['centerY'] = float(value)
        if key == 'axislength':
            frac['axisLen'] = float(value)
        if key == "type" and value != "mandelbrot":
            frac['type'] = str(value)

    if 'centerX' not in frac:
        raise RuntimeError("A required parameter is missing")
    elif 'centerY' not in frac:
        raise RuntimeError("A required parameter is missing")
    elif frac['axisLen'] <= 0000.0000:
        raise ValueError("axisLen must be positive")
    return tuple([Path(fname).stem, frac])


def main():
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


if __name__ == "__main__":
    main()

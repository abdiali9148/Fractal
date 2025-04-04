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


palette = ['#E1D89F', '#E0DA9E', '#E0DC9C', '#DFDE9B', '#DEDF9A', '#DBDE98',
           '#D8DE97', '#D4DD96', '#D1DD94', '#CDDC93', '#CADC92', '#C6DB91',
           '#C3DB8F', '#BFDA8E', '#BCD98D', '#B8D98B', '#B4D88A', '#B0D889',
           '#ACD788', '#A8D786', '#A4D685', '#A0D684', '#9CD582', '#98D481',
           '#94D480', '#8FD37F', '#8BD37D', '#87D27C', '#82D17B', '#7ED17A',
           '#79D078', '#77D07A', '#76CF7C', '#75CF7E', '#73CE80', '#72CD83',
           '#71CD85', '#70CC87', '#6ECB8A',    '#6DCB8C', '#6CCA8F', '#6BCA91',
           '#69C994', '#68C896', '#67C899', '#66C79C', '#65C79F', '#63C6A2',
           '#62C5A4', '#61C5A7', '#60C4AA', '#5FC3AD', '#5DC3B0', '#5CC2B3',
           '#5BC1B7', '#5AC1BA', '#59C0BD', '#57BFBF', '#56BABF', '#55B5BE',
           '#54B1BD', '#53ACBD', '#51A7BC', '#50A3BB', '#4F9EBB', '#4E99BA',
           '#4D94B9', '#4C8FB9', '#4A8AB8', '#4985B7', '#4880B7', '#487BB5',
           '#4876B4', '#4771B2','#476CB1','#4668AF','#4663AE', '#465EAC',
           '#455AAB', '#4556A9', '#4551A8', '#444DA6', '#4449A5', '#4345A3',
           '#4543A2', '#4843A1', '#4B429F', '#4E429E', '#51419C',
           '#54419B', '#574199', '#594098', '#5C4096', '#5E3F95', '#613F94',
           '#633F92', '#653E91', '#673E8F', '#6A3D8E', '#6C3D8C', '#6D3C8B',
           '#6F3C8A', '#713C88', '#733B87', '#753B85', '#763A84', '#783A83',
           '#793981', '#7A3980', '#7C387E', '#7D387D']

SIZE = 512  # the size of the image we will create is 512x512 pixels
MAX_ITERATIONS = 115


def pixelsWrittenSoFar(rows, cols): # fine
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
        return compute_iteration(c, escape_radius, MAX_ITERATIONS)


def PaintTheFractalsPixelsIntoTkinterWindow(fractal, window, img):

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
            print(pixelsWrittenSoFar(row, SIZE), end='\r', file=sys.stderr)
            row_colors = []  # Reset for the next row.


def castMbrotDataFileToHashMap(fname):
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


def __main__():
    """Main Mandelbrot Function"""
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        sys.exit(1)

    name,fractal = castMbrotDataFileToHashMap(sys.argv[1])
    print("Rendering {} fractal".format(name), file=sys.stderr)
    before = time.time()
    window = Tk()
    img = PhotoImage(width=512, height=512)
    PaintTheFractalsPixelsIntoTkinterWindow(fractal, window, img)
    img.write(f"{name}.png")
    after = time.time()
    mainloop()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    print(f"Saved image to file {name}.png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)


if __name__ == "__main__":
    __main__()

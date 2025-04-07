from tkinter import Tk, Canvas, PhotoImage, mainloop
from palettes import palette
import sys
from mandelbrot import pixel_color
from phoenix import phoenix_color_palette

SIZE = 512

MAX_ITERATIONS = 115


def mbrot_paint_fractal(fractal, window, img):

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


def show_status(rows, cols): # fine
    portion = (SIZE - rows) / SIZE
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return f'[{status_percent} {status_bar}]'


def create_window_and_image():
    """Create and return a Tk window and a PhotoImage object."""
    window = Tk()
    img = PhotoImage(width=SIZE, height=SIZE)
    return window, img


def p_show_status(rows):
    portion = (SIZE - rows) / SIZE
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return f'[{status_percent} {status_bar}]'


def phoenix_paint_fractal(fractal, window, img):
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
            color = phoenix_color_palette(point, fractal)
            row_colors.append(color)

        if col == SIZE - 1:
            img.put('{' + ' '.join(row_colors) + '}', to=(0, SIZE - row))
            window.update()  # Refresh the window to display the current row.
            print(p_show_status(row), end='\r', file=sys.stderr)


def run_window():
    mainloop()

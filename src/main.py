from image import phoenix_paint_fractal, mbrot_paint_fractal, create_window_and_image, run_window
import time
import sys
from parser import cast_hash_map

SIZE = 512


def main():
    """Main Mandelbrot Function"""
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        sys.exit(1)

    name,fractal = cast_hash_map(sys.argv[1])
    print("Rendering {} fractal".format(name), file=sys.stderr)
    before = time.time()
    window, img = create_window_and_image()
    if sys.argv[0] == 'src/mbrot_fractal.py':
        mbrot_paint_fractal(fractal, window, img)
    elif sys.argv[0] == 'src/phoenix_fractal.py':
        phoenix_paint_fractal(fractal, window, img)
    else:
        print("Please run either mbrot_fractal.py or phoenix_fractal.py")
        sys.exit()

    after = time.time()

    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{name}.png")
    print(f"Saved image to file {name}.png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)
    run_window()
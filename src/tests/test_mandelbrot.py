#!/usr/bin/env python3

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


import unittest
import os.path
from mandelbrot import pixel_color, compute_iteration
from mbrot_fractal import *
from palettes import palette
from image import MAX_ITERATIONS, show_status
from parser import cast_hash_map



class TestMandelbrot(unittest.TestCase):
    def setUp(self):
        self.here = os.path.dirname(__file__)

    def test_pixelColorOrIndex(self):
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""
        # test the pixel color...
        self.assertEqual('#7D387D', pixel_color(complex(0, 0), palette))
        self.assertEqual('#E0DC9C', pixel_color(complex(-0.751, 1.1075), palette))
        self.assertEqual('#CDDC93', pixel_color(complex(-0.2, 1.1075), palette))
        self.assertEqual('#79D078', pixel_color(complex(-0.75, 0.1075), palette))
        self.assertEqual('#59C0BD', pixel_color(complex(-0.748, 0.1075), palette))
        self.assertEqual('#6ECB8A', pixel_color(complex(-0.7562500000000001, 0.078125), palette))
        # ...or Index
        self.assertEqual(12, pixel_color(complex(-0.7562500000000001, -0.234375), None))
        self.assertEqual(10, pixel_color(complex(0.3374999999999999, -0.625), None))
        self.assertEqual(29, pixel_color(complex(-0.6781250000000001, -0.46875), None))
        self.assertEqual(4,  pixel_color(complex(0.4937499999999999, -0.234375), None))
        self.assertEqual(22, pixel_color(complex(0.3374999999999999, 0.546875), None))

    def test_pixelsWrittenSoFar(self):
        """Progress bar produces correct output"""
        self.assertEqual('[100% =================================]', show_status(1, 600))
        self.assertEqual('[ 99% =================================]', show_status(7, 7))
        self.assertEqual('[ 50% ================                 ]', show_status(257, 321))
        self.assertEqual('[ 50% =================                ]', show_status(256, 256))
        self.assertEqual('[ 80% ===========================      ]', show_status(100, 100))
        self.assertEqual('[-25%                                  ]', show_status(640, 480))
        self.assertEqual('[ 73% ========================         ]', show_status(137, 1000))
        self.assertEqual('[  0%                                  ]', show_status(512, 0))

    def test_castMbrotDataFileToHashMap(self):
        """Fractal configuration file parser behaves correctly"""
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/m/zero-axislen.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/m/bad-float-value.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/m/no-colons.frac")
        self.assertIsNotNone(cast_hash_map(f"{self.here}/m/mandelbrot.frac"))
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/m/bad-int-value.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/m/negative-axislen.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/m/too-many-colons.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/m/missing-value.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/m/commented-out-property.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/m/no-property-name.frac")

    def test_paletteLength(self):
        """Palette contains the expected number of colors"""
        self.assertEqual(111, len(palette))

    def test_palette_data_type(self):
        for color in palette:
            self.assertIsInstance(color, str)

    def test_count_return_type(self):
        count = compute_iteration(complex(0,0))
        self.assertIsInstance(count, int)

    def test_parser_file_not_found(self):
        self.assertRaises(FileNotFoundError, cast_hash_map, f"{self.here}/m/nonexistent.frac")

    def test_parser_returns_nonempty_dict(self):
        name , config = cast_hash_map(f"{self.here}/m/mandelbrot.frac")
        self.assertTrue(bool(config))

    def test_compute_iteration_origin(self):
        self.assertEqual(compute_iteration(complex(0, 0)), MAX_ITERATIONS - 1)

if __name__ == '__main__':
    unittest.main()

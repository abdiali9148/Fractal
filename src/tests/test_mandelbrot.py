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

from mbrot_fractal import PixelColorOrIndex
from mbrot_fractal import *
from mbrot_fractal import palette
from mbrot_fractal import MAX_ITERATIONS, pixelsWrittenSoFar
import mbrot_fractal


class TestMandelbrot(unittest.TestCase):
    def test_pixelColorOrIndex(self):
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""
        # test the pixel color...
        self.assertEqual('#7D387D', PixelColorOrIndex(complex(0, 0), palette))
        self.assertEqual('#E0DC9C', PixelColorOrIndex(complex(-0.751, 1.1075), palette))
        self.assertEqual('#CDDC93', PixelColorOrIndex(complex(-0.2, 1.1075), palette))
        self.assertEqual('#79D078', PixelColorOrIndex(complex(-0.75, 0.1075), palette))
        self.assertEqual('#59C0BD', PixelColorOrIndex(complex(-0.748, 0.1075), palette))
        self.assertEqual('#6ECB8A', PixelColorOrIndex(complex(-0.7562500000000001, 0.078125), palette))
        # ...or Index
        self.assertEqual(12, PixelColorOrIndex(complex(-0.7562500000000001, -0.234375), None))
        self.assertEqual(10, PixelColorOrIndex(complex(0.3374999999999999, -0.625), None))
        self.assertEqual(29, PixelColorOrIndex(complex(-0.6781250000000001, -0.46875), None))
        self.assertEqual(4,  PixelColorOrIndex(complex(0.4937499999999999, -0.234375), None))
        self.assertEqual(22, PixelColorOrIndex(complex(0.3374999999999999, 0.546875), None))

    def test_pixelsWrittenSoFar(self):
        """Progress bar produces correct output"""
        self.assertEqual('[100% =================================]', pixelsWrittenSoFar(1, 600))
        self.assertEqual('[ 99% =================================]', pixelsWrittenSoFar(7, 7))
        self.assertEqual('[ 50% ================                 ]', pixelsWrittenSoFar(257, 321))
        self.assertEqual('[ 50% =================                ]', pixelsWrittenSoFar(256, 256))
        self.assertEqual('[ 80% ===========================      ]', pixelsWrittenSoFar(100, 100))
        self.assertEqual('[-25%                                  ]', pixelsWrittenSoFar(640, 480))
        self.assertEqual('[ 73% ========================         ]', pixelsWrittenSoFar(137, 1000))
        self.assertEqual('[  0%                                  ]', pixelsWrittenSoFar(512, 0))

    def test_castMbrotDataFileToHashMap(self):
        """Fractal configuration file parser behaves correctly"""
        self.assertRaises(ValueError, mbrot_fractal.castMbrotDataFileToHashMap, "tests/m/zero-axislen.frac")
        self.assertRaises(ValueError, mbrot_fractal.castMbrotDataFileToHashMap, "tests/m/bad-float-value.frac")
        self.assertRaises(RuntimeError, mbrot_fractal.castMbrotDataFileToHashMap, "tests/m/no-colons.frac")
        self.assertIsNotNone(mbrot_fractal.castMbrotDataFileToHashMap("tests/m/mandelbrot.frac"))
        self.assertRaises(ValueError, mbrot_fractal.castMbrotDataFileToHashMap, "tests/m/bad-int-value.frac")
        self.assertRaises(ValueError, mbrot_fractal.castMbrotDataFileToHashMap, "tests/m/negative-axislen.frac")
        self.assertRaises(RuntimeError, mbrot_fractal.castMbrotDataFileToHashMap, "tests/m/too-many-colons.frac")

    def test_paletteLength(self):
        """Palette contains the expected number of colors"""
        self.assertEqual(111, len(palette))


if __name__ == '__main__':
    unittest.main()

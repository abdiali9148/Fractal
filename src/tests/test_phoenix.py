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


import os.path
import unittest
from palettes import grad
from parser import cast_hash_map
from phoenix import fractal_config, phoenix_color_palette


class TestPhoenix(unittest.TestCase):
    def setUp(self):
        self.here = os.path.dirname(__file__)
        fractal_name, self.fractal = cast_hash_map(f"{self.here}/p/phoenix.frac")

    def test_p(self):
        """Fractal configuration file parser behaves correctly"""
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/p/commented-out-property.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/p/bad-float-value.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/p/no-property-name.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/p/bad-int-value.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/p/zero-axislen.frac")
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/p/missing-value.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/p/too-many-colons.frac")
        self.assertIsNotNone(cast_hash_map(f"{self.here}/p/phoenix.frac"))
        self.assertRaises(ValueError, cast_hash_map, f"{self.here}/p/negative-axislen.frac")
        self.assertRaises(RuntimeError, cast_hash_map, f"{self.here}/p/no-colons.frac")

    def test_getColorFromPalette(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        self.assertEqual('#ffeca5', phoenix_color_palette(complex(0, 0), self.fractal))
        self.assertEqual('#ffe7af', phoenix_color_palette(complex(-0.751, 1.1075), self.fractal))
        self.assertEqual('#ffe8ac', phoenix_color_palette(complex(-0.2, 1.1075), self.fractal))
        self.assertEqual('#ffe5b2', phoenix_color_palette(complex(-0.750, 0.1075), self.fractal))
        self.assertEqual('#002277', phoenix_color_palette(complex(-0.1075, -0.748), self.fractal))
        self.assertEqual('#002277', phoenix_color_palette(complex(0.078125, -0.75625), self.fractal))
        self.assertEqual('#94ff51', phoenix_color_palette(complex(-0.234375, -0.75625), self.fractal))
        self.assertEqual('#ffe7af', phoenix_color_palette(complex(-0.625, 0.33749), self.fractal))
        self.assertEqual('#002277', phoenix_color_palette(complex(-0.46875, -0.678125), self.fractal))
        self.assertEqual('#ffe5b2', phoenix_color_palette(complex(-0.837, -0.406), self.fractal))
        self.assertEqual('#ffe7af', phoenix_color_palette(complex(-0.685, -0.186), self.fractal))

    def test_dictionaryGetter(self):
        """Names of properties in the configuration dictionary are as expected"""
        self.assertIsNone(fractal_config(self.fractal, 'absent'))
        self.assertIsNone(fractal_config(self.fractal, 'peacock'))
        self.assertIsNotNone(fractal_config(self.fractal, 'type'))
        self.assertIsNotNone(fractal_config(self.fractal, 'preal'))
        self.assertIsNotNone(fractal_config(self.fractal, 'pimag'))
        self.assertIsNotNone(fractal_config(self.fractal, 'creal'))
        self.assertIsNotNone(fractal_config(self.fractal, 'cimag'))

    def test_gradientLength(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(102, len(grad))

    def test_color_palette_return_type(self):
        fc = {
            'creal': 0.5667,
            'cimag': 0.0,
            'preal': -0.5,
            'pimag': 0.0
        }

        z = complex(0,0)
        return_type = phoenix_color_palette(z,fc)

        self.assertIsInstance(return_type, str)
        self.assertTrue(return_type.startswith('#'))
        self.assertEqual(len(return_type), 7)

        self.assertIn(return_type, grad)

    def test_grad_data_type(self):
        for color in grad:
            self.assertIsInstance(color, str)

    def test_phoenix_color_palette_format(self):
        color = phoenix_color_palette(complex(0, 0), self.fractal)
        self.assertIsInstance(color, str)
        self.assertTrue(color.startswith('#'))
        self.assertEqual(len(color), 7)

    def test_phoenix_config_contains_expected_keys(self):
        name, config = cast_hash_map(f"{self.here}/p/phoenix.frac")
        expected_keys = {"creal", "cimag", "preal", "pimag"}
        for key in expected_keys:
            self.assertIn(key, config)


if __name__ == '__main__':
    unittest.main()

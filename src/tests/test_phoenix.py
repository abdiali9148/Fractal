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
from phoenix_fractal import getColorFromPalette, grad, WHITE, f, p
from phoenix_fractal import getFractalConfigurationDataFromFractalRepositoryDictionary


class TestPhoenix(unittest.TestCase):
    def setUp(self):
        fractal_name, self.fractal = p("tests/p/phoenix.frac")

    def test_p(self):
        """Fractal configuration file parser behaves correctly"""
        self.assertRaises(RuntimeError, p, "tests/p/commented-out-property.frac")
        self.assertRaises(ValueError, p, "tests/p/bad-float-value.frac")
        self.assertRaises(RuntimeError, p, "tests/p/no-property-name.frac")
        self.assertRaises(ValueError, p, "tests/p/bad-int-value.frac")
        self.assertRaises(ValueError, p, "tests/p/zero-axislen.frac")
        self.assertRaises(ValueError, p, "tests/p/missing-value.frac")
        self.assertIsNotNone(p("tests/p/phoenix.frac"))
        self.assertRaises(ValueError, p, "tests/p/negative-axislen.frac")

    def test_getColorFromPalette(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        self.assertEqual('#ffeca5', getColorFromPalette(complex(0, 0), self.fractal))
        self.assertEqual('#ffe7af', getColorFromPalette(complex(-0.751, 1.1075), self.fractal))
        self.assertEqual('#ffe8ac', getColorFromPalette(complex(-0.2, 1.1075), self.fractal))
        self.assertEqual('#ffe5b2', getColorFromPalette(complex(-0.750, 0.1075), self.fractal))
        self.assertEqual('#002277', getColorFromPalette(complex(-0.1075, -0.748), self.fractal))
        self.assertEqual('#002277', getColorFromPalette(complex(0.078125, -0.75625), self.fractal))
        self.assertEqual('#94ff51', getColorFromPalette(complex(-0.234375, -0.75625), self.fractal))
        self.assertEqual('#ffe7af', getColorFromPalette(complex(-0.625, 0.33749), self.fractal))
        self.assertEqual('#002277', getColorFromPalette(complex(-0.46875, -0.678125), self.fractal))
        self.assertEqual('#ffe5b2', getColorFromPalette(complex(-0.837, -0.406), self.fractal))
        self.assertEqual('#ffe7af', getColorFromPalette(complex(-0.685, -0.186), self.fractal))

    def test_dictionaryGetter(self):
        """Names of properties in the configuration dictionary are as expected"""
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'absent'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'peacock'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'type'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'preal'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'pimag'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'creal'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(self.fractal, 'cimag'))

    def test_gradientLength(self):
        """Color palette contains the expected number of colors"""
        self.assertEqual(108, len(grad))


if __name__ == '__main__':
    unittest.main()

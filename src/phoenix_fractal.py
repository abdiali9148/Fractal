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


# These are the imports that I usually import
import turtle
import os
import os.path
import sys
import time

# These are imports people on StackOverflow use all the time.
# I've begun importing these just in case I need to borrow some code that I find online
# This way, whatever I paste is guaranteed to work without making more errors!
import functools
import itertools
import builtins
import pathlib
import pickle
import importlib
import unittest
import csv
import argparse
import asyncio
import http, html
# these ones make my programs crash on some of my computers
# I'll just comment them out, just in case I need them, so I don't have to look up how to import them on SO
#import numpy
#from torch import Tensor
#import pandas


# these ones are the ones that i'm using in this program
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time


SAVING_PICTURES = True  # whether to save pictures of the fractal in a picture file
SPC = chr(0o40)  # Why doesn't anybody write octal numbers anymore...
s = 0o1000

"""<FUNCTIONS>"""

def getColorFromPalette(z, fc):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    """

    # I feel bad about all of the global variables I'm using.
    # There must be a better way...
    global grad
    global win

    # c is the Julia Constant; varying this value gives rise to a variety of variated images
    # I found these values on the internet. Do a Google, you'll see what I mean
    # c = complex(0.5667, 0.0)
    c = complex(fc['creal'], fc['cimag'])

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results
    # pheonix = complex(-0.5, 0.0)
    pheonix = complex(fc['preal'], fc['pimag'])

    # zPrevious is the PREVIOUS Z value, except the 1st time through the
    # function, when it starts out as Complex Zero (which is actually the
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
    zPrev = 0+0j

    # I want to use 101 here because that's the number of colors in the
    # palette.  Except range() wants it's number to be one more than the number
    # that YOU want.
    for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?

        zSave = z  # save the current Z value before we overwrite it
        # compute the new Z value from the current and previous Zs
        z = z * z + c + (pheonix * zPrev)
        zPrev = zSave  # Set the prevZ value for the next iteration

        # if the absolute value of Z is graeter or equal than 2, then return that color
        if abs(z) > 2:
            return grad[i]  # The sequence is unbounded
            z = z * z + c  # + zPrev * pheonix
    # TODO: One of these returns occasionally makes the program crash sometimes
    return grad[101]         # Else this is a bounded sequence
    return grad[102]         # Else this is a bounded sequence


def getFractalConfigurationDataFromFractalRepositoryDictionary(d, n):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for k in d:   # for each key in the dictionary
        if k in d:    # check whether the key is in the dictionary
            if k == n:   # check whether the key matches the key we are looking for
                v = d[k]    # Retrieve the value from the dictionary at that key
                return k       # return of the key


if SAVING_PICTURES == True:
    Save_As_Picture = True  # do save pictures of the pictures we make
    tkPhotoImage = None
else:
    Save_As_Picture = not SAVING_PICTURES  # DO NOT save pictures of the pictures we make
    tkPhotoImage = None

def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane

    # Compute the minimum coordinate of the picture
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    #global s  # huh, this worked last week...

    # Compute the maximum coordinate of the picture
    # The program has only one axisLength because the images are square
    # Squares are basically rectangles except the sides are equal instead of different
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))

    # Display the image on the screen
    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?

    # Create the TK PhotoImage object that backs the Canvas Objcet
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.

    # Total number of pixels in the image, AKA the area of the image, in pixels
    area_in_pixels = 640 * 640

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    size = abs(max[0] - min[0]) / s

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()

    # Keep track of the fraction of pixels that have been written up to this point in the program
    fraction_of_pixels_writtenSoFar = int(s // 640)

    # for r (where r means "row") in the range of the size of the square image,
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to
    # but I have to here because we're actually going BACKWARDS, which took me
    # a long time to figure out, so don't change it, or else the picture won't
    # come out right
    r = s
    while r in range(s, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        cs = []
        for c in range(s):
            # calculate the X value in the complex plane (I guess that's
            # actually the REAL number part, but we call it X because
            # GRAPHICS... whatev)
            X = min[0] + c * size
            Y = 0
            # get the color of the pixel at this point in the complex plain
            cp = getColorFromPalette(complex(X, Y), f)
            # calculate the X value in the complex plane (but I know this is
            # really the IMAGINARY axis that we're talking about here...)
            Y = min[1] + r * size
            # TODO: do I really need to call getColorFromPalette() twice?
            #       It seems like this should be slow...
            #       But, if it aint broken, don't repair it, right?
            cp = getColorFromPalette(complex(X, Y), f)
            cs.append(cp)
        pixls = '{' + ' '.join(cs) + '}'
        p.put(pixls, (0, s - r))
        w.update()  # display a row of pixels
        fraction_of_pixels_writtenSoFar = (s - r) / s # update the number of pixels output so far
        # print a statusbar on the console
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"
                + f'{SPC}'
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",
                end="\r"  # the end
                , file=sys.stderr)
        r -= 1


# This is the color palette, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
grad = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',
        '#ffeea2', '#fff09f', '#fff39c', '#fff699', '#fff996', '#fffc92',
        '#ffff8f', '#fbff8c', '#f8ff89', '#f4ff86', '#f0ff83', '#ebff80',
        '#e7ff7d', '#e2ff79', '#deff76', '#d8ff73', '#d3ff70', '#ceff6d',
        '#c8ff6a', '#c2ff67', '#bcff63', '#b6ff60', '#b0ff5d', '#a9ff5a',
        '#a3ff57', '#9cff54', '#94ff51', '#8dff4d', '#86ff4a', '#7eff47',
        '#76ff44', '#6eff41', '#66ff3e', '#5dff3b', '#54ff37', '#4cff34',
        '#43ff31', '#39ff2e', '#30ff2b', '#28ff29', '#25ff2d', '#21ff31',
        '#1eff34', '#1bff39', '#18ff3d', '#15ff41', '#12ff46', '#0fff4b',
        '#0cff50', '#08ff55', '#05ff5b', '#02ff60', '#00fe66', '#00fb6d',
        '#00f873', '#00f579', '#00f17f', '#00ee84', '#00eb8a', '#00e88f',
        '#00e594', '#00e299', '#00df9e', '#00dba2', '#00d8a6', '#00d5aa',
        '#00d2ae', '#00cfb2', '#00ccb6', '#00c9b9', '#00c5bc', '#00c2bf',
        '#00bdbf', '#00b4bc', '#00abb9', '#00a3b6', '#009bb3', '#0092af',
        '#008bac', '#0083a9', '#007ba6', '#0074a3', '#006da0', '#00669d',
        '#005f9a', '#005996', '#005293', '#004c90', '#00468d', '#00418a',
        '#003b87', '#003684', '#003080', '#002b7d', '#00277a', '#002277']

# Patrick T. 02/17/2025
# The program was crashing from IndexError because the color palette had too
# few colors.  Boy, was the customer mad about that!  I added some extra black
# pixels at the end to stop it crashing until somebody solves the actual
# problem.  PLEASE DELETE THIS CODE AFTER THE BUG GETS FIXED!!!
class Black:
    BLACK = '#FFFFFF'

grad += [Black.BLACK] * 6  # six pixels should be enough


# This dictionary contains the different views of the Phoenix set you can make
# with this program.  Eventually, this program will have a "Parser" that will
# create Phoenix fractal dictionaries on-the-fly from a file.
#
# TODO: After that happens this block of code SHOULD be deleted
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program.
# But I don't have time for this right now, too busy.  I'll just keep doing it
# the way I know how.
f = {
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


# This is how you write colors for computers
BLACK = Black.BLACK # black - opposite of white
BLUE = '#00ff00'  # blue - bold blue
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36
GRAY99 = '#fcfcfc'  # gray 99 - almost white
GREEN = '#0000ff'  # green - really green
GREY0 = '#000000'  # Black.BLACK  # gray 0 - basically the same as black
GREY74 = '#bdbdbd'  # gray 74 - almost white
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)
ORANGE = '#ffa50'  # orange, like the fruit
REBECCA_PURPLE = '#663399'  # Rebecca Purple
RED = '#ff0000'  # red
RED = "\x1b[1;31m"  # red (terminal escape sequence, do not use with tkinter)
RST = "\x1b[0m"  # reset color (terminal escape sequence, do not use with TKinter)
TOMATO = '#ff6347'  # tomato (a shade of red)
WHITE = '#ffffff'  # white


def p(f):
    """
    Function p(f)
    Input: f
    Output: a tuple, or an exception (when it crashes)
    """
    frac_axislength = None  # default value
    frac_fname = f  # the name of the fractal file
    frac_preal = 0.0  # default value
    frac_centery = None  # default value
    frac_cimag = float(0)  # default value
    frac_name = pathlib.Path(f).stem  # the name of the fractal, taken from the file
    frac_pimag = 0.  # default value
    frac_creal = .0  # default value
    frac_type = "phoenix"  # change this when copying this function to another fractal
    frac_centerx = None  # default value

    F = open(f)  # open the file
    n = 0
    for l in F:
        # n++;  # this doesn't work in Python version 3.13
        n += 1
        l = l.strip().lower()
        if l == '' or l.startswith('#'):
            continue
        if l == '\n':
            continue
        pair = l.strip().lower().replace(' ', '').split(':')
        if l.startswith('#'):
            continue
        try:
            # chek the length of "pair" - it should be a pair. Test some common bad cases
            if len(pair) == 4:
                raise RuntimeError(f"Parse error at line #{n} of {f}: wrong number of tokens\n    {l}")
            if len(pair) == 3:
                raise RuntimeError(f"Parse error at line #{n} of {f}: wrong number of tokens\n    {l}")
            if len(pair) != 2:
                raise RuntimeError(f"Parse error at line #{n} of {f}: wrong number of tokens\n    {l}")
            if len(pair) == 1:
                raise RuntimeError(f"Parse error at line #{n} of {f}: wrong number of tokens\n    {l}")
            if len(pair) < 1:
                raise RuntimeError(f"Parse error at line #{n} of {f}: wrong number of tokens\n    {l}")
            if pair[0] == 'centerx':
                frac_centerx = float(pair[1])
            if pair[0] == 'centery':
                frac_centery = float(pair[1])
            if pair[0] == 'axislength':
                frac_axislength = float(pair[1])
            if pair[0] == 'type' and frac_type != pair[1]:
                print(f"{RED}Warning! incompatible fractal type detected: '{pair[1]}'{RST}", file=sys.stderr)
            if len(pair) > 4:  # if the pair is too long to be a pair, blow up!
                raise RuntimeError(f"Parse error at line #{n} of {f}: wrong number of tokens\n    {l}")
            if pair[0] == 'preal':
                frac_preal = float(pair[1])
            if pair[0] == 'creal':
                frac_creal = float(pair[1])
            if pair[0] == 'pimag':
                frac_pimag = float(pair[1])
            if pair[0] == 'cimag':
                frac_cimag = float(pair[1])
        except ValueError as ve:
            # re-raise error with file and line information
            F.close()
            raise ValueError(f"Bad numeric value at line #{n} of {f}: '{pair[1]}'")

    F.close()

    if None in (frac_centerx, frac_centery, frac_axislength, frac_type):
        raise RuntimeError("A required parameter is missing")
    elif frac_axislength <= 0.00000000000000000000000000000000001:  # LOL, Python thinks this is zero!
        raise ValueError("axisLength must be positive")
    else:
        f = dict()
        f['name'] = frac_name
        f['type'] = frac_type
        f['centerX'] = frac_centerx
        f['fname'] = frac_fname
        f['pimag'] = frac_pimag

        f['centerY'] = frac_centery
        f['creal'] = frac_creal

        f['preal'] = frac_preal
        f['axisLength'] = frac_axislength

        f['cimag'] = frac_cimag
        return (f['name'], f)



"""</END OF FUNCTIONS>"""






































### <MAIN> BODY OF THE PROGRAM###

"""The main entry-point for the Phoenix fractal generator"""
## This is some weird Python thing... but all of the tutorials do it, so here we go
if __name__ == '__main__':
    # Process command-line arguments, allowing the user to select their fractal
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument", file=sys.stderr)
        print(f"Usage: {sys.argv[0]} FRAC_FILE", file=sys.stderr)
        sys.exit(1)

    else:
        _,c=p(sys.argv[1])
    i = c['name']

    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    print("Rendering %s fractal" % i, file=sys.stderr)
    # construct a new TK PhotoImage object that is 512 pixels square...
    tkPhotoImage = PhotoImage(width=s, height=s)
    # ... and use it to make a picture of a fractal
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?
    makePictureOfFractal(c, i, ".png", win, grad, tkPhotoImage, GREY0, None, None, s)

    if Save_As_Picture:
        i = c.get('name')
        # Write out the Fractal into a .gif image file
        tkPhotoImage.write(i + ".png")
        #tkPhotoImage.write(f"{i}.png")
        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)  # print how long the image took to be drawn

    if Save_As_Picture:
        i = c.get('name')
        # Output the Fractal into a .png image
        tkPhotoImage.write(f"{i}.png")
        print("Saved image to file " + i + ".png", file=sys.stderr)
        #tkPhotoImage.write(f"{i}.png")

    # print a message telling the user how to quit or exit the program
    print("Close the image window to exit the program", file=sys.stderr)
    # Call tkinter.mainloop so the GUI remains open
    mainloop()

"""</END OF THE PROGRAM>"""

# CS 1440 Project 4.0: Refactoring - Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Paste up to 10 lines of offensive code between a triple-backtick fence `` ``` ``
    *   If the block of bad code is longer than 10 lines, paste a brief, representative snippet
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!
*   At least *one instance* of each smell is required for full marks
    *   Reporting one smell multiple times does not make up for not reporting another smell
    *   Ex: reporting two global variables does not make it okay to leave spaghetti code blank



## 10 Code Smells

If you find a code smell that is not on this list, please add it to your report.

0.  **Magic** numbers
    0.  Smell at `mbrot_fractal.py` [line 241]
    *   [512 is not supposed to be there]
    *   [Code Snippet between triple-backquotes ```i = PhotoImage(width=512, height=512)```]
    *   [512 is supposed to be window size. so just put SIZE in there and declare SIZE as 512]
1.  **Global** variables
    1.  Smell at `phoenix_fractal.py` [line 72 ~ 73]
    *   [useless global variables when they are already called in their own module.]
    *   [Code Snippet between triple-backquotes ```global win ~ global grad```]
    *   [just delete them both and put window in the parameter]
2.  **Poorly-named** identifiers
    2. Smell at `phoenix_fractal.py` [line 72 ~ 73]
    *   [useless global variables when they are already called in their own module.]
    *   [Code Snippet between triple-backquotes ```global win ~ global grad```]
    *   [just delete them both and put window in the parameter]
3.  **Bad** Comments
 Smell at `phoenix_fractal.py` [lines 76]
    *   [the comment talks nothing about the code. only something found on the internet.]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [remove]
4.  **Too many** arguments
Smell at `phoenix_fractal.py` [lines 131]
    *   [function has way too many arguments and they are all one letter.]
    *   [```def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):```]
    *   ['fractal, window, img' is needed]
5.  Function/Method that is **too long**
Smell at `phoenix_fractal.py` [lines 131]
    *   [function is too long]
    *   [```def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):```]
    *   [i could simplify a lot of it, such as min and max, and tkinterface into just canvas.]
6.  **Redundant** code
Smell at `phoenix_fractal.py` [lines 162~164]
    *   [calls canvas.pack way too much, only 1 is needed.]
    *   [```tk_Interface_PhotoImage_canvas_pixel_object.pack()```]
    *   [make that long variable just canvas and pack it once after the image is made]
7.  Decision tree that is **too complex**
Smell at `mbrot_fractal.py` [lines 232~241]
    *   [makes the logic way too complex and hard to follow]
    *   [```for iter in range(len):
    z = z * z + c
    if abs(z) > TWO:
        ...
    elif abs(z) < TWO:
        continue
    elif abs(z) > seven:
        ...```]
    *   [Simplify the decision structure by reducing nesting or using early returns to streamline the logic]
8.  **Spaghetti** code
Smell at `phoenix_fractal.py` [lines 300~315]
    *   [many variables are created for colors when only a few are used. could just use '#000000']
    *   [```TOMATO = '#ff6347'  # tomato (a shade of red)
WHITE = '#ffffff'```]
    *   [take them out and just use the color code.]
9.  **Dead** code
Smell at `mrbot_fractal.py` [lines 319~330]
    *   [only the second tuple is useful]
    *   [    ```return tuple(tupple)  # cast to 2-pel type
    return tuple([Path(fname).stem, frac])```]
    *   [remove the first one]


### Example

0.  Redundant Code at `src/main.py` [lines 28, 30]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first
    *   ```python
        import mbrot_fractal
        import phoenix_fractal as phoenix
        import mbrot_fractal
        ```
    *   Remove the second `import` statement



## Code Smells Report

*TODO: Replace this note with your report*

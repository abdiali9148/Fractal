# CS 1440 Project 4: Refactoring & Object-Oriented Design

*Note: this file is a placeholder for your own notes.  When seeking help from the TAs or tutors replace the text in this file with a description of your problem and push it to your repository on GitLab*


## 4.0: Refactoring
*   [Instructions](./instructions/4.0-README.md)
    *   [Tkinter Installation & Troubleshooting](./instructions/4.0-Tkinter.md)
    *   [How to Submit this Project](./instructions/How_To_Submit.md)
*   [Project Requirements](./instructions/4.0-Project_Requirements.md)
*   [Understanding Fractals](./instructions/4.0-Fractals.md)
*   [Running Unit Tests](./instructions/4.0-Running_Unit_Tests.md)

## 4.1: Object-Oriented Design

*   [Instructions](./instructions/4.1-README.md)
    *   [How to Submit this Project](./instructions/How_To_Submit.md)
*   [Project Requirements](./instructions/4.1-Project_Requirements.md)
*   The [Fractal Gallery](./data/README.md)
*   [Invalid Fractal Configuration Files](./invalid/README.md)


## Get The Starter Code

*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$` (that represents your shell's prompt).
    *   Replace `USERNAME` with your GitLab username, `LAST` and `FIRST` with your names as used on Canvas.

```bash
$ git clone git@gitlab.cs.usu.edu:duckiecorp/cs1440-falor-erik-proj4 cs1440-proj4
$ cd cs1440-proj4
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-proj4
$ git push -u origin --all
```


## Overview

Our firm has been contracted to help a mathematician bring his amazing "one-million dollar" idea to life.  Our client specializes in the field of complex dynamics, which, frankly, is well above my pay grade, but so is programming to him.  He has a passion for mathematics education and wants to take his programs to the K-12 system to teach middle and high-school students all about the beauty of complex numbers and repeated, tedious calculations.  I didn't have the heart to tell him that there are already dozens of web sites doing what he wants to do for free; if his inability to use Google keeps us in steady work, who am I to set him straight?

His plan was to create a system of programs capable of drawing a variety of fractals.  He made it through the second prototype before realizing that making user-friendly software is as challenging as grasping complex dynamics, and decided to get some professional help.  This is where we come in.  Our task is to adapt his prototypes into a complete *Programming Systems Product*.  There are two DuckieCorp teams assigned to the project:

0.  Team zero (your team) will document and clean up the mathematician's starter code and eventually add new features
1.  Team one will create a brand-new, user-friendly graphical interface

It is not strictly necessary for you to understand the math behind fractals in order to refactor this program.  To be completely honest with you, I don't understand them myself.  If you are really dying to know more about fractals, read [Understanding Fractals](./instructions/4.0-Fractals.md).  But don't let ignorance stop you from refactoring; if you are patient and careful, you can clean up the program even if you don't fully grasp how it works.


## Running The Starter Code

The starter code is runnable out-of-the-box.  If it doesn't work on your computer, check the [Tkinter document](./instructions/4.0-Tkinter.md) for instructions.  If you still have trouble, contact DuckieCorp management with a bug report.

When you launch the program, a window opens, and a fractal image is drawn from top to bottom.  When the drawing is complete, a copy of the image is saved as a PNG file in the current directory.  Close the window to exit the program.

This command draws a fractal using the Mandelbrot algorithm according to the parameters from the file `data/mandelbrot.frac`:
*(You may need to use `python3` instead of `python` on your system)*

```bash
$ python src/mbrot_fractal.py data/mandelbrot.frac
```

This command uses the Phoenix algorithm to draw a picture called "Monkey Knife Fight":

```bash
$ python src/phoenix_fractal.py data/p-monkey-knife-fight.frac
```

The [Project 4.0 Requirements](./instructions/4.0-Project_Requirements.md#user-interface) explains the command line interface in detail.



## Running Unit Tests

The starter code contains 8 **non-trivial** test cases, all of which pass (the 15 tests in `src/tests/test_assertions.py` don't count; they are merely examples).

*   The unit tests are scripts in the directory `src/tests`.
*   You may run the unit tests through PyCharm or the shell.
    *   We will run the tests from a shell when we grade your submission.  You should make sure they work this way, too!
*   Full instructions are found in [Running Unit Tests](./instructions/4.0-Running_Unit_Tests.md).



## What The Heck Are Fractals?

Read [Understanding Fractals](./instructions/4.0-Fractals.md).

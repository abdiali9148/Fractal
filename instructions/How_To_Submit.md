# CS 1440 Project 4: Refactoring & Object-Oriented Design - How to Submit This Project

* [When to Submit Your Work](#when-to-submit-your-work)
* [Repository Naming Convention](#repository-naming-convention)
* [Repository Layout](#repository-layout)
* [Verify Your Submission](#verify-your-submission)
* [Python Version](#python-version)


I am very particular about the format of your project submissions.

*   Yes, I have my reasons.
*   No, I do not make exceptions.
*   Deviations from these guidelines **will result in penalties**.

<details>
<summary><strong>Why am I so picky about how you submit your homework?</strong></summary>

0.  **Programming is a detail-oriented activity**.  The sooner you embrace this fact, the happier you will be.
1.  In the workforce **your boss and coworkers will be just as picky as I am** about how you turn in your work.  Perhaps more so.  It is not good enough if your code "just works" on your computer.  Your code needs to "just work" on their computers, too.
2.  In a large class **every second adds up**.  If it takes 60 seconds for a grader to figure out how to run each student's submission, then in a class of 120 students two hours is spent just getting started.  Since there are five projects in this class, we would spend more than an entire work-day on this trivial task.

</details>



## When to Submit Your Work

*   Projects are due by 11:59:59 PM on the posted due date according to the clock on my GitLab server.
*   A submission arrives when it is *pushed* to my GitLab server.
    *   Commits pushed _after_ the due date are late.
    *   Commits bearing timestamps _before_ the due date but are *pushed* _after_ the due date are late.
*   You can push your code to GitLab as many times as you want.
    *   Commits pushed to GitLab after the due date will not be graded.


### Which clock judges lateness?

The clock on **gitlab.cs.usu.edu** keeps the official time for the class.  When you push to the server you will see a "receipt" in your console:

```
***********************************************************************
*           __  ________  __  _____                ____    _          *
*          / / / / __/ / / / / ___/__  __ _  ___  / __/___(_)         *
*         / /_/ /\ \/ /_/ / / /__/ _ \/  ' \/ _ \_\ \/ __/ /          *
*         \____/___/\____/  \___/\___/_/_/_/ .__/___/\__/_/           *
*                                         /_/                         *
*  ,/         \,                                                      *
* ((__,-"""-,__))                                                     *
*  `--)~   ~(--`                                                      *
* .-'(       )'-,                                                     *
* `--`d\   /b`--`  Big Blue says:                                     *
*     |     |                                                         *
*     (6___6)  Your submission arrived Wed 18 Jan 2023 21:17:25 MDT   *
*      `---`                                                          *
*                                                                     *
***********************************************************************
```

*   The time stamp comes from the GitLab server's clock.
*   This is the official time of your submission's arrival.
*   If you don't see this receipt, make sure that you are pushing your code to **my** GitLab server at `gitlab.cs.usu.edu`.


## Repository Naming Convention

Your work is submitted by using Git to push code to repositories (a.k.a. "repos", a.k.a.  "projects") on the course GitLab server.  I made a program to help me find your submission out of the thousands on the server.  It is very important that the name of your repo follows this pattern:

`cs1440-LAST-FIRST-proj#`

*   Use hyphens `-` to separate words.
    *   **Do not** use underscores `_`, dots `.` or other punctuation.
*   The course number `cs1440` comes first.
*   Name your submission such that _LAST_ and _FIRST_ correspond to your "Full Name" in Canvas.  Find your "Full Name" in Canvas by browsing to `Account -> Settings`.
    *   Two first or last names can be used; separate them with hyphens `-`.
    *   You *do not* need to include your middle name, unless it is part of your "Full Name" in Canvas, or if there is a classmate who shares your first and last name.
    *   If you do include your middle name, it comes after your first name: `cs1440-LAST-FIRST-MIDDLE-proj#`.
*   At the end the project is specified as `proj#`
    *   **Do not** use any other variation of the word "project".


#### Good repo names:

*   `cs1440-osullivan-siobhan-proj1` (Siobhán O'Sullivan's project #1)
*   `cs1440-jones-bill-proj4` (Bill Jones's project #4)
*   `cs1440-rubio-gould-teresa-proj2` (Teresa Rubio-Gould's project #2 - multiple surnames are OK)
*   `cs1440-hardin-kinsley-donovan-proj3` (Kinsley D. Hardin's project #3 submission, includes his middle name to distinguish from the other Kinsley Hardin (no relation) in this class)


#### Bad repo names:

*   `cs1000-osullivan-siobhan-proj1` (wrong course number: this is **cs1440**, not **cs1000**)
*   `1440-jones-bill-proj4` (invalid course number: it must begin with **cs**)
*   `cs-1440-jones-bill-proj4` (invalid course number: spell it as **cs1440**, not **cs-1440**)
*   `cs1440-rubio-gould-teresa-prj2` (**proj#** is spelled wrong)
*   `cs1440-rubio-gould-teresa-proj-2` (**proj#** is spelled wrong)
*   `cs1440-rubio-gould-teresa-project2` (**proj#** is spelled wrong)
*   `cs1440-pixelwarrior5010-proj2` (**pixelwarrior5010** isn't your "Full Name" in Canvas)
*   `cs1440.jones.bill.proj4` (periods separate words instead of hyphens)

When you get these details wrong it appears that you made no submission at all.

On the other hand, you may create repositories for your other courses on my GitLab server.  This naming convention avoids confusion between those repositories and your homework for this course.


<details>
<summary><strong>Rationale</strong></summary>

0.  Naming your GitLab project with your Canvas "full name" avoids confusion.  Some of our graders are not native English speakers and don't know that `Dick == Richard`, `Lexi == Alexandria`, `Billy == William`, `Chuck == Charles`, `Becky == Rebecca`, etc.
1.  To deal with the large volume of submissions each semester I wrote a program to find your repo by its URL.  The naming convention is rigid because it is a simple program and is very easily confused.
2.  In GitLab a project's *name* can differ from its *path* or URL.  It is possible to fix mistakes in the naming of your repo.  Just make sure that you change its **Path** instead of its **Name**.  *See below*

</details>


### Changing your repository's URL on GitLab

If you gave your project the wrong URL, you can fix it in GitLab before the due date with no penalty.

*Note that the project's **URL** is different from its **name**; see the next tip for details about renaming a project*

0.  Navigate to the project on the web and click the gear icon at the bottom of the left sidebar (the Settings menu), and click *General*
1.  Scroll all the way to the bottom until you find the **Advanced** section.  Click `Expand`
    *   _Do not change the **Project name** that you see at the top of this page!_
2.  Scroll to the middle of the **Advanced** section until you see a box titled **Change path**.  Put the correct project name into this box and click the `Change path` button.
3.  Back on your PC update your project's remote URL.  Assuming your GitLab remote is nicknamed `origin`, this command will update the URL (substitute your own details in this command):
    ```
    $ git remote set-url origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-proj#
    ```
4.  After changing the path you *must* make another push before my submission collection program can notice the change.
    *   You may need to edit a file and create a new commit so that you can do a push.
    *   If you don't know what to change, just make a small, cosmetic change in one of the README.md files.



## Repository Layout

0.  **Do not start from scratch**
    *   Clone the starter code repository and continue from there.
1.  A well-organized submission makes it **easy for us to help you** and grade your work.
    *   Some files and directories **are required** to be present.
    *   Some files and directories **must not** be part of your submission.
    *   **Do not** remove or re-arrange files given to you in the starter code unless told to do so.
2.  This is what a good submission looks like:
    *   ```tree --charset=ascii
        cs1440-proj4
        |-- data
        |   |-- assets/
        |   |-- README.md
        |   |-- ...
        |   |-- phoenix.frac
        |   `-- spider.frac
        |-- demo
        |   `-- interactive.py
        |-- doc
        |   |-- 4.0-Plan.md
        |   |-- 4.1-Plan.md
        |   |-- Manual.md
        |   |-- Signature.md
        |   `-- Smells.md
        |-- instructions
        |   |-- 4.0-Project_Requirements.md
        |   |-- 4.0-README.md
        |   |-- 4.1-Project_Requirements.md
        |   |-- 4.1-README.md
        |   |-- assets/
        |   |-- Fractals.md
        |   |-- How_To_Submit.md
        |   |-- Running_Unit_Tests.md
        |   `-- Tkinter.md
        |-- invalid/
        |-- README.md
        `-- src
            |-- mbrot_fractal.py
            |-- phoenix_fractal.py
            |-- phoenix.png
            |-- run_tests.py
            `-- tests
                |-- __init__.py
                |-- test_assertions.py
                |-- test_mandelbrot.py
                `-- test_phoenix.py
        ```


### Files and directories your repository _MUST_ contain

0.  A `README.md` in the top-level directory
    *   This file is *not* read-only, and you *may* modify it
    *   If you have any special instructions or explanations for your grader, put them at the top of this file
1.  A file named `.gitignore`.  This file may be hidden from file listings in the shell
    *   The contents of `.gitignore` are explained in detail below
2.  `src/`
    *   Contains your source code
3.  `instructions/`
    *   Contains my instructions to you
    *   Don't modify files in this directory; consider this area read-only
4.  `doc/`
    *   Contains documentation written by you.  You may edit the files provided by us, and add new ones
    *   `Signature.md` - the *Sprint Signature*
        *   Record a **brief** log of your accomplishments every day that you worked on the project
        *   One or two sentences per day suffice
    *   Keep this directory **tidy**
        *   Delete extraneous and out-of-date files so your grader doesn't have to waste time figuring out what's what


### Files and directories your repository _MAY_ contain

0.  `.idea/` created by PyCharm
1.  `.vscode/` created by Visual Studio Code
2.  Any other subdirectories needed to organize your work as you see fit


### Files your repository _MUST NOT_ contain

0.  Directories containing pre-compiled files or other generated files created by your IDE or build tools (e.g. `venv`, `.pyc` files, etc.).  Exceptions to this are your IDE's project subdirectory:
    * `.idea/` created by PyCharm.
    * `.vscode/` created by Visual Studio Code.
1.  Zip files or archives.
2.  Backup files or folders.
3.  Screenshots.
4.  Any other detritus left behind from your experimentation.
5.  Extremely large files.  What is considered "extremely large" depends upon the project, but a good rule of thumb is to avoid committing files larger than 20 megabytes.

**Before you make your final submission, clean up your repository!**


### Keep your Git repository clean with `.gitignore`

A special file at the root of the starter code repository called `.gitignore` helps you avoid committing unwanted files and directories.  Each line specifies a filename pattern that Git refuses to add to the repository.  The `.gitignore` file in the starter code repository looks like this:

```
# Show Your Work log files
*showyourwork*
_showyourwork.sqlite

# Common IDE configuration files
.idea
.vscode
*.sw[pon]
*~

# Virtual environments
.venv
venv

# Python cache files
*.pyc
__pycache__

# Other files to ignore for good practice
*.bak
*.csv
*.png
*.zip
.DS_Store
```

You should leave this file as it is.  Do not rename it, as Git is particular about how its name is spelled.  Contact a TA or the instructor if you break your `.gitignore` file.

<details>
<summary><strong>Rationale</strong></summary>

### What difference do the names and locations of my files make?

*   The starter code repo is organized to help you quickly find the files you need to read or edit.
*   Your boss and coworkers will expect you to maintain the organization of code that you write and maintain at your job.
*   This organization prevents guesswork on the part of tutors, TAs and the instructor when you have questions about your code.  We will be able to run your program without fuss and will see exactly the same output on our computer that you get on yours.
*   This layout facilitates quick and efficient grading, freeing us to give you more detailed feedback on your submissions.


### Why do I make you write **doc/Plan.md**?

*   How do you know what code to write if you don't know what program you are creating?
*   You write this file for *you*.  Failing to plan is planning to fail.
    *   Students who write detailed plans learn more and get better scores.
    *   Students who write the SDP as an afterthought right before they turn in an project have just wasted hours of their precious lives.
*   I cannot make you into a good programmer; that is something you must do for yourself.
    *   The exercise of writing this document forces you to be thoughtful and intentional about programming.  That is how you will become a good programmer.


### Why do I need to write **doc/Signature.md**?

*Don't Git's commit messages make this file redundant?*

No.  Git commit messages serve a different purpose than the Sprint Signature.

*   Git commit messages describe just a small portion of your work, often just a few lines of code.
    *   You should make several commits each day, each with its own message.
*   The Sprint Signature captures a big-picture summary of your daily work, and helps you stay on-task:
    *   If your daily summary consists of pointless fiddling, you will be more focused tomorrow.
    *   Reviewing the sprint signature helps you recognize when you are getting stuck in the project.
*   Writing a daily log encourages you to work at least a little bit every day, helping you become consistent.


### Do you even look at these files?

Yes.

</details>



## Verify Your Submission

Sometimes there are files on your computer that are not committed to Git.  Consequently, those files are not present when we clone your repository, which causes your program to crash.

An easy way to avoid this is to re-clone your repository from GitLab into a fresh location on your computer and give it one final test from there.  This lets you experience your submission just as the graders will.

0.  In your shell, navigate into a different directory and `git clone` your repository.
    *   You can find the URL to clone by running `git remote -v` in your original repository, or on the GitLab website.
1.  Prevent *Gitception* by not `git clone`ing when your shell is already inside a Git repo.
    *   *Always* run `git status` before using `git clone`!  You want it to show you this error:
    *   ```
        $ git status
        fatal: Not a git repository (or any parent up to mount point /)
        Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
        ```
2.  Thoroughly test this fresh copy of your program:
    *   Run your program from the command-line instead of your IDE; we don't grade your code with an IDE.
    *   Run the command-line examples shown in the instructions.
    *   Run any tests included with the starter code.
    *   Run through the test cases in the **Testing** section of your Software Development Plan.



## Python Version

*   Graders will run your code against the official distribution of Python version 3.9 or greater from https://python.org
*   Python version 2 has reached its end of life.
*   Code written for Python 2.x is not acceptable in this class.

For this class you must either:

*   Install Python version 3.9 or greater on your own computer
*   Find a computer with the correct version of Python
    *   Computers in CS labs and the Engineering Computer lab have the correct version of Python.


### How can I tell if I have the right version of Python installed?

Run `python --version` from the command line:

```
$ python --version
Python 3.13.1
```

If this reports a version number beginning with 2, run `python3` instead:

```
$ python3 --version
Python 3.13.1
```

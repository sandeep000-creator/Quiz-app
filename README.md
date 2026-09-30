# Python Quiz App

A command-line multiple choice quiz written in Python. Built as my project for the VITyarthi *Build Your Own Project* evaluation at VIT Bhopal University.

## Overview

The program asks for the player's name, lets them choose a subject, then asks 10 randomly chosen multiple-choice questions. After each answer it says whether it was right, and at the end it prints the score with a short comment. It uses only the Python standard library.

## Features

- Asks for the player's name and uses it in every message.
- Two quiz categories: **General Knowledge** (20-question bank) and **CSE** (10-question bank).
- 10 random, non-repeating questions per round.
- Input validation for name, menu choice and answers (only `a`, `b`, `c` or `d` is accepted).
- Instant feedback, with the correct option shown when the answer is wrong.
- Halfway progress message and a final score banner with a comment.
- Replay option without restarting the program.

## Technologies / Tools Used

- Python 3 (standard library only, the `random` module)
- Programiz Online Python Compiler for development and testing
- Git and GitHub for version control

## Project Structure

```
.
├── main.py          # the complete quiz program
├── README.md        # this file
└── statement.md     # problem statement, scope, users, features
```

## How to Install and Run

1. Install Python 3.8 or newer from [python.org](https://www.python.org/downloads/). Check with `python --version`. No extra packages are needed.
2. Clone the repository and move into the folder:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
3. Run the program:
   ```bash
   python main.py
   ```

You can also paste `main.py` into any online Python compiler and press Run.

## How to Test

Testing is manual and input-based. Run the program and try these:

| Step | What to enter | Expected result |
|------|---------------|-----------------|
| 1 | Press Enter on the name prompt | Asks for the name again |
| 2 | Enter `3` at the subject menu | Asks for just 1 or 2 |
| 3 | Enter `z` as an answer | Asks for a, b, c or d again |
| 4 | Answer wrongly on purpose | Wrong message plus the right option |
| 5 | Finish all 10 questions | Score banner and comment |
| 6 | Type `no` at the replay prompt | Goodbye message and the program exits |

## Author

Sandeep Kumar, VIT Bhopal University

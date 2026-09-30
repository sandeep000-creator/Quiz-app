# Problem Statement

## Project: Python Quiz App (Command-Line)

## Problem Statement

Students learning Python and computer science fundamentals usually revise by re-reading notes, which is passive. There is no quick way to test yourself, get an immediate answer check and see an overall score without opening a website that needs a login or a heavy app.

This project builds a lightweight program that runs anywhere Python runs. It lets a student practise multiple-choice questions, tells them straight away whether each answer was right, and ends with a score.

## Scope of the Project

**In scope**

- A console program written in Python 3, run from a terminal or an online compiler.
- Two subjects: General Knowledge (20 questions in the bank) and CSE / Python basics (10 questions in the bank).
- Ten randomly chosen, non-repeating questions per round, each with four options (a, b, c, d).
- Validation of every input (name, subject choice, answer letter).
- Instant feedback, a halfway progress message, a final score and a score-based comment.
- Option to replay without restarting the program.

**Out of scope**

- Graphical or web interface.
- Saving scores or user accounts between runs.
- Timed quizzes, difficulty levels, or adding questions from inside the program.

## Target Users

- First and second year engineering students (especially CSE) who want quick Python and general-knowledge practice.
- Beginners who want a complete, readable example of a small Python program.
- Anyone preparing for a short quiz who needs a fast self-check.

## High-Level Features

- Personalised greeting using the player's name.
- Subject selection menu (General Knowledge or CSE).
- Random selection of 10 questions per round using `random.sample()`.
- Input validation with friendly re-prompts instead of crashes.
- Varied correct and wrong feedback messages; the right option is shown after a wrong answer.
- Halfway progress message and a final score banner with a comment based on percentage.
- Play-again loop.

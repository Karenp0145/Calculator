# 🧮 PyGame Calculator

A graphical calculator built in **Python using PyGame**, combining a custom calculation engine with an interactive interface inspired by real calculators.

---

## Overview

This project features:
- A custom calculator engine (no `eval()`)
- Correct operator precedence
- Parentheses handling
- Implicit multiplication (e.g. `5(10+4)`)
- A grid-based PyGame interface with clickable buttons

---

## Project Structure

```text
Calculator/
│
├── calculatrice.py   # Calculator engine (parsing & evaluation)
├── main.py           # PyGame graphical interface
├── .gitignore
└── README.md
```

---

## Features

### Calculator Engine
- Expression tokenization
- Operator precedence
- Parentheses evaluation
- Implicit multiplication support

### PyGame Interface
- Clickable buttons
- Grid layout
- Color-coded keys
- Expression display
- Error handling

---

## How to Run

```bash
pip install pygame
python main.py

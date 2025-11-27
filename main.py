#!/usr/bin/python3 -B

import sys
import importlib
import os
import requests
from datetime import datetime

def help(exit_code=0):
    print("Usage: ./main.py day [input]")
    exit(exit_code)

def error(message):
    print(f"[ERROR]: {message}")
    print("")
    help(exit_code=1)

def download_input_if_not_present(day, file_path):
    if os.path.exists(file_path):
        return
    
    event_year = datetime.now().year
    session_cookie = os.getenv("AOC_SESSION_COOKIE")

    assert session_cookie is not None and len(session_cookie) == 128, "Invalid session cookie"

    data = requests.get(f'https://adventofcode.com/{event_year}/day/{day}/input', cookies={'session': session_cookie}).text
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(data)

if len(sys.argv) < 2:
    error("day parameter missing")

[_, day, *other_args] = sys.argv

if day == "-h" or day == "--help":
    help()

day = int(day)

if day < 1 or day > 25:
    error("day parameter must be an int in [1, 25]")

input_filename = f"inputs/{day}.input"
if len(other_args) > 0:
    input_filename = other_args[0]
else:
    download_input_if_not_present(day, input_filename)

solver = importlib.import_module(f"solutions.{day}")

print("")
with open(input_filename, 'r') as f:
    if hasattr(solver, "solve_first"):
        print(f"First problem of {day}:")
        print(f"Solution = {solver.solve_first(f)}")
    else:
        print(f"No solution implemented in solver for first problem of {day}")
    print("")
    
with open(input_filename, 'r') as f:
    if hasattr(solver, "solve_second"):
        print(f"Second problem of {day}:")
        print(f"Solution = {solver.solve_second(f)}")
    else:
        print(f"No solution implemented in solver for second problem of {day}")
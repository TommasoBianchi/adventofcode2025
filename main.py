#!/usr/bin/python3 -B

import sys
import importlib
import os
import requests
from datetime import datetime
from time import perf_counter

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

def solve_day(day, input_override=None):
    input_filename = f"inputs/{day}.input"
    if input_override is not None:
        input_filename = input_override
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

def main():
    if len(sys.argv) < 2:
        error("day parameter missing")

    [_, day, *other_args] = sys.argv

    if day == "-h" or day == "--help":
        help()

    day = int(day)

    if day < 0 or day > 25:
        error("day parameter must be an int in [1, 25], or 0 to run all available solutions")

    if day > 0:
        solve_day(day, input_override=other_args[0] if len(other_args) > 0 else None)
    else:
        all_days = [int(filename.replace('.py', '')) for filename in os.listdir("solutions") if filename not in ["template.py", "__pycache__"]]
        solve_times = []
        for day in sorted(all_days):
            start = perf_counter()
            solve_day(day)
            solve_times.append(perf_counter() - start)
        print("")
        print("Solve times:")
        for i, solve_time in enumerate(solve_times):
            print(f"Day {i + 1}: {solve_time * 1000:8.0f} milliseconds")
        print("-" * 30)
        print(f"Total: {sum(solve_times) * 1000:8.0f} milliseconds")

if __name__ == "__main__":
    main()

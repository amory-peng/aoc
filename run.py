import difflib
from importlib import import_module
import sys
import contextlib
import os

dir = sys.argv[1]
ex = 1 if len(sys.argv) > 2 else 0

os.chdir(dir)
year, day = dir.split('/')

example_file = 'example.txt'
expected_file = 'expected.txt'

runner = import_module(f'{year}.{day}.run')

# 1. run example
if os.path.exists(example_file):
  print("1. Running example...")
  runner.run(example_file)
else:
  print("no example file found, skipping")

print()
# 2. run input
input_file = "input.txt"
if ex:
  print("ran example only")
elif os.path.exists(input_file):
  print("2. Running input...")
  runner.run(input_file)
else:
  print("no input file found, skipping")

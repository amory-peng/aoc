import heapq
from collections import defaultdict
from functools import reduce
from math import inf
import os
import contextlib

input_file = 'input.txt'


def run(file):
  print('part1: ')
  part1(file)
  # print('part2: ')
  # part2(file)


class Rock:
  shapes = {
    'fl': [(0, 0), (0, 1), (0, 2), (0, 3)],
    'pl': [(-1, 0), (-1, 1), (-1, 2), (-2, 1), (0, 1)],
    'an': [(0, 0), (0, 1), (0, 2), (-1, 2), (-2, 2)],
    'vt': [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    'sq': [(0, 0), (0, 1), (-1, 0), (-1, 1)]
  }

  order = ['fl', 'pl', 'an', 'vt', 'sq']

  def __init__(self, height, shape, floor=0):
    self.start = (height, 2)
    self.floor = floor
    i, j = self.start

    self.spaces = [(i + di, j + dj) for (di, dj) in self.shapes[shape]]
    # we always want to know the height (sort by row)
    self.spaces.sort()

  def next_jet(self, dir):
    dj = -1 if dir == '<' else 1
    return [(i, j + dj) for (i, j) in self.spaces]

  def next_fall(self):
    di = 1
    return [(i + di, j) for (i, j) in self.spaces]

  def collide(self, nspaces, other_rocks):
    # check floor/wall collision
    for (ni, nj) in nspaces:
      if ni >= self.floor or nj < 0 or nj >= 7:
        return True
    # check other rocks
    if other_rocks:
      for other in other_rocks:
        if [space for space in nspaces if space in other.spaces]:
          return True
    return False

  def top(self):
    return self.spaces[0][0]

  def move(self, nspaces):
    self.spaces = nspaces

  def __lt__(self, other):
    return self.top() < other.top()


def draw(rocks, floor):
  output_file = 'output.txt'

  os.remove(output_file)
  with open(output_file, 'w') as o:
    with contextlib.redirect_stdout(o):
      height = rocks[0].top() if rocks else -5
      height = -5 if height > -5 else height
      spaces = set()
      for rock in rocks:
        spaces = spaces | set(rock.spaces)
      for i in range(height, floor):
        row = []
        for j in range(0, 7):
          if (i, j) in spaces:
            row.append('#')
          else:
            row.append('.')
        print('|' + ''.join(row) + '| ')


def get_new_floor(rocks, floor):
  grid = [floor for _ in range(7)]
  for rock in rocks:
    for (i, j) in rock.spaces:
      grid[j] = min(grid[j], i)

  return max(grid)


def part1(file):
  wind = []
  for line in open(file).readlines():
    wind = [c for c in line.strip()]

  def run_tick(tick, rock: Rock, other_rocks):
    # move in dir if possible
    dir = wind[tick % len(wind)]
    # move in dir
    nspaces = rock.next_jet(dir)
    # check for collisions
    if not rock.collide(nspaces, other_rocks):
      rock.move(nspaces)
    nspaces = rock.next_fall()
    if not rock.collide(nspaces, other_rocks):
      rock.move(nspaces)
      return True
    else:
      return False

  prev_flat = None
  rocks = []
  tick = 0
  top = 0
  num_rocks = 0
  while not num_rocks == 281 + 729:
    if num_rocks % 500 == 0:
      print(num_rocks)
    # check if we need to update floor, then remove all rocks with greater(less) height
    top = 0 if not rocks else rocks[0].top()
    shape = Rock.order[num_rocks % 5]
    rock = Rock(top - 4, shape, 0)

    # draw([rock] + rocks, floor)
    while run_tick(tick, rock, rocks):
      tick += 1
    tick += 1
    heapq.heappush(rocks, rock)
    num_rocks += 1

  draw(rocks, 0)
  print("num_rocks:", num_rocks)
  print("ans", -rocks[0].top())

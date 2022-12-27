from collections import defaultdict, deque
from math import inf


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def any_neighbors(elf, elves):
  i, j = elf
  for di in range(-1, 2):
    for dj in range(-1, 2):
      if (di, dj) == (0, 0):
        continue
      if (i + di, j + dj) in elves:
        return True
  return False


def play_round(elves, direction_order):
  # new pos -> set of elves
  moves = defaultdict(set)

  for i, j in elves:
    # 0. check neighbors
    if not any_neighbors((i, j), elves):
      moves[(i, j)].add((i, j))
    else:
      # 1. propose move
      proposed = False
      for direction, ne_checks in direction_order:
        if proposed:
          break
        neighbor = False
        for (di, dj) in ne_checks:
          if (i + di, j + dj) in elves:
            neighbor = True
            break
        if not neighbor:
          di, dj = direction
          moves[(i + di, j + dj)].add((i, j))
          proposed = True
      if not proposed:
        moves[(i, j)].add((i, j))
  # 2. check collisions
  future_elves = set()
  for move, elves in moves.items():
    if len(elves) > 1:
      future_elves = future_elves | elves
    else:
      future_elves.add(move)
  # 3. rotate diff order
  direction_order.append(direction_order.popleft())
  return (future_elves, direction_order)


def get_rect(elves):
  start_row = inf
  start_col = inf
  end_row = -inf
  end_col = -inf
  for (i, j) in elves:
    start_row = min(start_row, i)
    end_row = max(end_row, i)
    start_col = min(start_col, j)
    end_col = max(end_col, j)
  h = end_row - start_row + 1
  w = end_col - start_col + 1
  print(h * w)
  return h * w


def print_grid(elves):
  for i in range(0, 15):
    row = []
    for j in range(0, 20):
      c = '#' if (i, j) in elves else '.'
      row.append(c)
    print(''.join(row))
  print('')


def part1(file):
  i = 0
  elves = set()
  for line in open(file).readlines():
    for j, c in enumerate(line.strip()):
      if c == '#':
        elves.add((i, j))
    i += 1

  direction_order = deque([
    # direction, ne_checks
    # north
    [(-1, 0), [(-1, -1), (-1, 0), (-1, 1)]],
    # south
    [(1, 0), [(1, -1), (1, 0), (1, 1)]],
    # west
    [(0, -1), [(-1, -1), (0, -1), (1, -1)]],
    # east
    [(0, 1), [(-1, 1), (0, 1), (1, 1)]]
  ])

  for i in range(10):
    elves, direction_order = play_round(elves, direction_order)

  print("res", get_rect(elves) - len(elves))


def part2(file):
  i = 0
  elves = set()
  for line in open(file).readlines():
    for j, c in enumerate(line.strip()):
      if c == '#':
        elves.add((i, j))
    i += 1

  direction_order = deque([
    # direction, ne_checks
    # north
    [(-1, 0), [(-1, -1), (-1, 0), (-1, 1)]],
    # south
    [(1, 0), [(1, -1), (1, 0), (1, 1)]],
    # west
    [(0, -1), [(-1, -1), (0, -1), (1, -1)]],
    # east
    [(0, 1), [(-1, 1), (0, 1), (1, 1)]]
  ])

  round = 0
  while True:
    ne_elves, direction_order = play_round(elves, direction_order)
    round += 1
    if ne_elves == elves:
      break
    elves = ne_elves

  print("res", round)

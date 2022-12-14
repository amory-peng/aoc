import os


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def parse(line):
  res = []
  for str in line.strip().split('->'):
    res.append([int(c) for c in str.split()[0].split(',')])
  return res


def draw(cave, pos=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  m = len(cave)
  n = len(cave[0])
  if pos:
    x, y = pos
    cave[y][x] = '~'
  # only want a window
  for row in cave:
    print(''.join(row[350:650]))
  if pos:
    x, y = pos
    cave[y][x] = '.'


def part1(file):
  m = 1000
  n = 1000
  cave = [['.' for _ in range(n)] for _ in range(m)]

  for line in open(file).readlines():
    rock_coords = parse(line)
    for i in range(len(rock_coords) - 1):
      (x0, y0), (x1, y1) = sorted([rock_coords[i], rock_coords[i + 1]])
      (dx, dy) = (0, 1) if y0 != y1 else (1, 0)
      while x0 != x1 or y0 != y1:
        cave[y0][x0] = '#'
        x0 += dx
        y0 += dy
      cave[y1][x1] = '#'

  def drop_sand(x, y):
    # attempt to move downwards
    deltas = [(0, 1), (-1, 1), (1, 1)]
    falling = True
    while falling:
      # input()
      # draw(cave, (x, y))
      for (dx, dy) in deltas:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          return False
        if cave[ny][nx] == '.':
          x = nx
          y = ny
          falling = True
          break
        else:
          falling = False

    # we didn't move, set sand in cave
    cave[y][x] = 'o'
    return True

  res = 0
  while drop_sand(500, 0):
    res += 1
  print(res)


def part2(file):
  all_rock_coords = []
  floor_pos = 2
  for line in open(file).readlines():
    rock_coords = parse(line)
    for (x, y) in rock_coords:
      floor_pos = max(floor_pos, y + 2)
    all_rock_coords.append(rock_coords)

  m = floor_pos + 1
  n = 1000
  cave = [['.' for _ in range(n)] for _ in range(m)]
  cave[-1] = ['#'] * n

  for rock_coords in all_rock_coords:
    for i in range(len(rock_coords) - 1):
      (x0, y0), (x1, y1) = sorted([rock_coords[i], rock_coords[i + 1]])
      (dx, dy) = (0, 1) if y0 != y1 else (1, 0)
      while x0 != x1 or y0 != y1:
        cave[y0][x0] = '#'
        x0 += dx
        y0 += dy
      cave[y1][x1] = '#'
  sand_start = (500, 0)

  def drop_sand(pos):

    x, y = pos
    # attempt to move downwards
    deltas = [(0, 1), (-1, 1), (1, 1)]
    falling = True
    while falling:
      falling = False
      # input()

      for (dx, dy) in deltas:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          return False
        if cave[ny][nx] == '.':
          x = nx
          y = ny
          falling = True
          break

    # we didn't move, set sand in cave
    if (x, y) == sand_start:
      return False
    cave[y][x] = 'o'
    return True

  res = 1
  while drop_sand(sand_start):
    res += 1
  draw(cave)
  print(res)

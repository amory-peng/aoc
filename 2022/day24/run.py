def run(file):
  # print('part1: ')
  # part1(file)
  print('part2: ')
  part2(file)


directions = {
  '>': (0, 1),
  '<': (0, -1),
  'v': (1, 0),
  '^': (-1, 0)
}


def part1(file):
  i = 0
  # (pos, direction)
  blizzards = set()
  for line in open(file).readlines():
    line = line.strip()
    w = len(line)
    for j, c in enumerate(line):
      if c in directions:
        pos = (i, j)
        direction = directions[c]
        blizzards.add((pos, direction))
    i += 1
  m = i
  n = w

  def move_blizzards(blizzards):
    ne_blizzards = set()
    for pos, direction in blizzards:
      i, j = pos
      di, dj = direction
      ni = i + di
      nj = j + dj
      if ni == 0:
        ni = m - 2
      if ni == m - 1:
        ni = 1
      if nj == 0:
        nj = n - 2
      if nj == n - 1:
        nj = 1
      ne_blizzards.add(((ni, nj), direction))
    return ne_blizzards

  def print_grid(blizzards):
    for i in range(m):
      row = []
      for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
          row.append('#')
        elif (i, j) in [blizzard for (blizzard, _) in blizzards]:
          row.append('B')
        else:
          row.append('.')
      print(''.join(row))

  def possible_moves(pos, blizzard_positions):
    i, j = pos
    moves = set()
    for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
      ni = i + di
      nj = j + dj
      if ni <= 0 or ni == m - 1 or nj <= 0 or nj == n - 1:
        if not ((ni, nj) == start or (ni, nj) == end):
          continue
      if (ni, nj) in blizzard_positions:
        continue
      moves.add((ni, nj))

    return moves

  start = (0, 1)
  end = (m - 1, n - 2)
  print(start, end)
  queue = set([start])
  steps = 0
  while True:
    if steps % 1000 == 0:
      print(steps, len(queue))
    # input()
    new_queue = set()
    steps += 1
    blizzards = move_blizzards(blizzards)
    blizzard_positions = [blizzard for blizzard, _ in blizzards]
    for pos in queue:
      if pos == end:
        print("res", steps - 1)
        return
      new_queue = new_queue | possible_moves(pos, blizzard_positions)
    queue = new_queue


def part2(file):
  i = 0
  # (pos, direction)
  blizzards = set()
  for line in open(file).readlines():
    line = line.strip()
    w = len(line)
    for j, c in enumerate(line):
      if c in directions:
        pos = (i, j)
        direction = directions[c]
        blizzards.add((pos, direction))
    i += 1
  m = i
  n = w

  def move_blizzards(blizzards):
    ne_blizzards = set()
    for pos, direction in blizzards:
      i, j = pos
      di, dj = direction
      ni = i + di
      nj = j + dj
      if ni == 0:
        ni = m - 2
      if ni == m - 1:
        ni = 1
      if nj == 0:
        nj = n - 2
      if nj == n - 1:
        nj = 1
      ne_blizzards.add(((ni, nj), direction))
    return ne_blizzards

  def print_grid(blizzards):
    for i in range(m):
      row = []
      for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
          row.append('#')
        elif (i, j) in [blizzard for (blizzard, _) in blizzards]:
          row.append('B')
        else:
          row.append('.')
      print(''.join(row))

  def possible_moves(pos, blizzard_positions):
    i, j = pos
    moves = set()
    for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
      ni = i + di
      nj = j + dj
      if ni <= 0 or ni >= m - 1 or nj <= 0 or nj >= n - 1:
        if not ((ni, nj) == start or (ni, nj) == end):
          continue
      if (ni, nj) in blizzard_positions:
        continue
      moves.add((ni, nj))

    return moves

  start = (0, 1)
  end = (m - 1, n - 2)

  def travel(start, end, blizzards):
    print(start, end)
    queue = set([start])
    steps = 0
    while True:
      if steps % 100 == 0:
        print(steps, len(queue))
      if end in queue:
        print("steps", steps)
        return blizzards
      # input()
      new_queue = set()
      steps += 1
      blizzards = move_blizzards(blizzards)
      blizzard_positions = [blizzard for blizzard, _ in blizzards]
      for pos in queue:
        new_queue = new_queue | possible_moves(pos, blizzard_positions)
      queue = new_queue

  blizzards = travel(start, end, blizzards)
  blizzards = travel(end, start, blizzards)
  blizzards = travel(start, end, blizzards)

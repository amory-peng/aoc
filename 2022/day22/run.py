from collections import deque


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):

  facing_map = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
  }

  res = 0
  map = []
  d_str = ""
  end_of_map = False
  for line in open(file).readlines():
    if '.' in line:
      map.append([c for c in line[:-1]])
    else:
      d_str = line.strip()
  directions = deque([])
  i = 0
  while i < len(d_str):
    c = d_str[i]
    if c == 'R' or c == 'L':
      directions.append(c)
      i += 1
    else:
      j = i
      while j < len(d_str) and d_str[j] != 'R' and d_str[j] != 'L':
        j += 1
      directions.append(int(d_str[i:j]))
      i = j
  n = max([len(row) for row in map])
  m = len(map)
  print(len(directions))
  new_map = [[' ' for _ in range(n)] for _ in range(m)]
  for i, row in enumerate(map):
    for j, c in enumerate(row):
      new_map[i][j] = c
  map = new_map
  start_row = map[0]
  start_col = start_row.index('.')
  pos = (0, start_col)
  facing = 0

  while directions:

    direction = directions.popleft()
    if direction == 'R':
      facing += 1
      if facing == 4:
        facing = 0
    elif direction == 'L':
      facing -= 1
      if facing == -1:
        facing = 3
    else:
      di, dj = facing_map[facing]
      for _ in range(direction):
        i, j = pos
        ni = i + di
        nj = j + dj
        # find next pos:
        if ni < 0 or ni == m or nj < 0 or nj == n or map[ni][nj] == ' ':
          nni = i - di
          nnj = j - dj
          while 0 <= nni < m and 0 <= nnj < n and not map[nni][nnj] == ' ':
            nni = nni - di
            nnj = nnj - dj
          ni, nj = nni + di, nnj + dj

        if map[ni][nj] == '.':
          pos = (ni, nj)
        elif map[ni][nj] == '#':
          break

  print("ans", 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing)


def part2(file):
  facing_map = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
  }

  res = 0
  map = []
  d_str = ""
  for line in open(file).readlines():
    if '.' in line:
      map.append([c for c in line[:-1]])
    else:
      d_str = line.strip()
  directions = deque([])
  i = 0
  while i < len(d_str):
    c = d_str[i]
    if c == 'R' or c == 'L':
      directions.append(c)
      i += 1
    else:
      j = i
      while j < len(d_str) and d_str[j] != 'R' and d_str[j] != 'L':
        j += 1
      directions.append(int(d_str[i:j]))
      i = j
  n = max([len(row) for row in map])
  m = len(map)
  print(n, m)
  new_map = [[' ' for _ in range(n)] for _ in range(m)]
  for i, row in enumerate(map):
    for j, c in enumerate(row):
      new_map[i][j] = c
  map = new_map
  print(len(directions))
  h = 49
  # edge transition is (transform position, new direction)
  # 12 edges -> 24 transitions
  wrap_map = {
    (1, 2): (lambda i, j: (i, 0), 0),
    (2, 1): (lambda i, j: (i, h), 2),
    (1, 6): (lambda i, j: (j, i), 0),
    (6, 1): (lambda i, j: (j, i), 1),
    (1, 3): (lambda i, j: (0, j), 1),
    (3, 1): (lambda i, j: (h, j), 3),
    (1, 5): (lambda i, j: (h - i, 0), 0),
    (5, 1): (lambda i, j: (h - i, 0), 0),

    (5, 6): (lambda i, j: (0, j), 1),
    (6, 5): (lambda i, j: (h, j), 3),
    (6, 2): (lambda i, j: (0, j), 1),
    (2, 6): (lambda i, j: (h, j), 3),
    (2, 3): (lambda i, j: (j, h), 2),
    (3, 2): (lambda i, j: (h, i), 3),
    (3, 5): (lambda i, j: (0, i), 1),
    (5, 3): (lambda i, j: (j, 0), 0),

    (4, 2): (lambda i, j: (h - i, h), 2),
    (2, 4): (lambda i, j: (h - i, h), 2),
    (4, 3): (lambda i, j: (h, j), 3),
    (3, 4): (lambda i, j: (0, j), 1),
    (4, 5): (lambda i, j: (i, h), 2),
    (5, 4): (lambda i, j: (i, 0), 0),
    (4, 6): (lambda i, j: (j, h), 2),
    (6, 4): (lambda i, j: (h, i), 3)
  }

  transitions = {
    1: [2, 3, 5, 6],
    2: [4, 3, 1, 6],
    3: [2, 4, 5, 1],
    4: [2, 6, 5, 3],
    5: [4, 6, 1, 3],
    6: [4, 2, 1, 5]
  }
  plane_starts = [(0, 50), (0, 100), (50, 50), (100, 50), (100, 0), (150, 0)]
  planes = {}

  for p, (start_row, start_col) in enumerate(plane_starts):
    pl = p + 1
    p_map = [[None for _ in range(h + 1)] for _ in range(h + 1)]
    for i in range(h + 1):
      for j in range(h + 1):
        p_map[i][j] = map[start_row + i][start_col + j]
    planes[pl] = p_map

  # for pl, plmap in planes.items():
  #   print("pl: ", pl)
  #   label = [format(i, '2d') for i in range(h + 1)]
  #   print(' '.join(label))
  #   for i, row in enumerate(plmap):
  #     new_row = [c for c in row]
  #     new_row += [str(i)]
  #     print('  '.join(new_row))

  def run(start_plane, start_pos, start_facing):

    plane = start_plane
    pos = start_pos
    facing = start_facing

    def draw():
      pointers = ['➡️', '⬇️', '⬅️', '⬆️']
      draw_map = planes[plane]
      print("plane: ", plane, "direction:", direction, "pos:", pos)
      label = [format(i, '2d') for i in range(h + 1)]
      print(' '.join(label))
      for (i, row) in enumerate(draw_map):
        draw_row = []
        for j, c in enumerate(row):
          if (i, j) == pos:
            draw_row.append(pointers[facing])
          else:
            draw_row.append(c)
        print('  '.join(draw_row + [str(i)]))
      input()

    print("start plane", plane, "start pos", pos, "start facing", facing)
    for direction in directions:
      # draw()
      if direction == 'R':
        facing += 1
        if facing == 4:
          facing = 0
      elif direction == 'L':
        facing -= 1
        if facing == -1:
          facing = 3
      else:

        for _ in range(direction):
          di, dj = facing_map[facing]
          i, j = pos
          ni = i + di
          nj = j + dj
          n_plane = plane
          nfacing = facing
          if nj > h:
            n_plane = transitions[plane][0]
          if ni > h:
            n_plane = transitions[plane][1]
          if nj < 0:
            n_plane = transitions[plane][2]
          if ni < 0:
            n_plane = transitions[plane][3]
          if not n_plane == plane:
            transform, nfacing = wrap_map[(plane, n_plane)]
            ni, nj = transform(i, j)
            print("transition!", 'old plane', plane, "nplane", n_plane,
                  'old pos', pos, 'npos', (ni, nj), "facing", facing, "nfacing", nfacing)
          if planes[n_plane][ni][nj] == '.':
            pos = (ni, nj)
            plane = n_plane
            facing = nfacing
          elif planes[n_plane][ni][nj] == '#':
            # print('hit wall')
            break
    # draw()
    print("end plane", plane, "end pos", pos, "end facing", facing)
    print(plane_starts[plane - 1])
    r, c = plane_starts[plane - 1]
    res = 1000 * (r + pos[0] + 1) + 4 * (c + pos[1] + 1) + facing
    print(res)

  plane = 1
  pos = (0, 0)
  facing = 0
  run(plane, pos, facing)
  # for plane in range(1, 7):
  #   for pos in [(0, 15), (15, 0), (49, 15), (15, 49)]:
  #     for facing in range(4):

  # run(plane, pos, facing)

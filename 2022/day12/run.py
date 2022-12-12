from collections import deque
from math import inf


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def get_elevation(c):
  if c == 'S':
    return ord('a')
  elif c == 'E':
    return ord('z')
  return ord(c)


def part1(file):
  map = []
  for line in open(file).readlines():
    map.append([c for c in line.strip()])
  # print(res)
  m = len(map)
  n = len(map[0])
  start, end = None, None
  # get starting position
  for i in range(m):
    for j in range(n):
      if map[i][j] == 'S':
        start = (i, j)
      elif map[i][j] == 'E':
        end = (i, j)
  # shortest path with bfs
  queue = [start]
  seen = set()
  steps = 0
  while queue:
    new_queue = []
    for pos in queue:
      if pos == end:
        print(steps)
        return
      if pos in seen:
        continue
      seen.add(pos)
      i, j = pos
      for (di, dj) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj
        if ni < 0 or nj < 0 or ni == m or nj == n:
          continue
        curr_elevation = get_elevation(map[i][j])
        next_elevation = get_elevation(map[ni][nj])
        if next_elevation - curr_elevation > 1:
          continue
        new_queue.append((ni, nj))

    steps += 1
    queue = new_queue


def part2(file):
  map = []
  for line in open(file).readlines():
    map.append([c for c in line.strip()])
  # print(res)
  m = len(map)
  n = len(map[0])
  starts, end = [], None
  # get starting position
  for i in range(m):
    for j in range(n):
      if map[i][j] == 'S' or map[i][j] == 'a':
        starts.append((i, j))
      elif map[i][j] == 'E':
        end = (i, j)
  res = inf
  # shortest path with bfs
  for start in starts:
    queue = [start]
    seen = set()
    steps = 0
    while queue:
      new_queue = []
      for pos in queue:
        if pos == end:
          # print(start, steps)
          res = min(steps, res)
        if pos in seen:
          continue
        seen.add(pos)
        i, j = pos
        for (di, dj) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
          ni = i + di
          nj = j + dj
          if ni < 0 or nj < 0 or ni == m or nj == n:
            continue
          curr_elevation = get_elevation(map[i][j])
          next_elevation = get_elevation(map[ni][nj])
          if next_elevation - curr_elevation > 1:
            continue
          new_queue.append((ni, nj))

      steps += 1
      queue = new_queue
  print(res)

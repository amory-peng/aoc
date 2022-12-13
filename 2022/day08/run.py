def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):
  res = 0
  grid = []
  for line in open(file).readlines():
    line = line.strip()
    grid.append([int(c) for c in line])

  m = len(grid)
  n = len(grid[0])
  seen = set()

  def look(i, j, di, dj, curr_max):
    if i < 0 or i == m or j < 0 or j == n:
      return

    if grid[i][j] > curr_max:
      seen.add((i, j))
      curr_max = grid[i][j]
    ni = i + di
    nj = j + dj
    look(ni, nj, di, dj, curr_max)

  for j in range(n):
    # from first row, look down
    look(0, j, 1, 0, -1)
    # from last row, look up
    look(m - 1, j, -1, 0, -1)
  for i in range(m):
    # from first col, look right
    look(i, 0, 0, 1, -1)
    # from last col, look left
    look(i, n - 1, 0, -1, -1)

  print(len(seen))


def part2(file):
  grid = []
  for line in open(file).readlines():
    line = line.strip()
    grid.append([int(c) for c in line])

  m = len(grid)
  n = len(grid[0])

  scenic_scores = [[1 for _ in range(n)] for _ in range(m)]

  def look(i, j, di, dj, height):
    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
      return 0

    ni = i + di
    nj = j + dj
    if grid[ni][nj] >= height:
      return 1

    return 1 + look(ni, nj, di, dj, height)

  for i in range(m):
    for j in range(n):
      for (di, dj) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        scenic_scores[i][j] *= look(i, j, di, dj, grid[i][j])
  res = max([max(row) for row in scenic_scores])
  print(res)

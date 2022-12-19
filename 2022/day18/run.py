def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def check_neighbor(coord, grid, mat='L'):
  x, y, z = coord
  open = 6
  for d in [1, -1]:
    if grid[x + d][y][z] == mat:
      open -= 1
    if grid[x][y + d][z] == mat:
      open -= 1
    if grid[x][y][z + d] == mat:
      open -= 1
  return open


def part1(file):
  grid = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

  for line in open(file).readlines():
    x, y, z = [int(c) for c in line.strip().split(',')]
    grid[x][y][z] = 'L'

  sides = 0
  for i, x in enumerate(grid):
    for j, y in enumerate(x):
      for k, _ in enumerate(y):
        if grid[i][j][k]:
          sides += check_neighbor((i, j, k), grid)
  print(sides)


def part2(file):
  # three states:
  # L: lava, O: open air, None: unknown
  n = 23
  grid = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]

  for line in open(file).readlines():
    x, y, z = [int(c) for c in line.strip().split(',')]
    grid[x][y][z] = 'L'

  def dfs(x, y, z, visited):
    # if we're out of bounds then we're free
    if x < 0 or y < 0 or z < 0 or x >= n or y >= n or z >= n:
      return True
    if grid[x][y][z] == 'L':
      return False
    visited.add((x, y, z))
    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
      nx, ny, nz = x + dx, y + dy, z + dz
      if (nx, ny, nz) in visited:
        continue
      if dfs(nx, ny, nz, visited):
        return True

    return False

  for i, x in enumerate(grid):
    for j, y in enumerate(x):
      for k, _ in enumerate(y):
        if not grid[i][j][k] == "L":
          visited = set()
          if not dfs(i, j, k, visited):
            for (x, y, z) in visited:
              grid[x][y][z] = 'L'

  lava = 0
  for i, x in enumerate(grid):
    for j, y in enumerate(x):
      for k, _ in enumerate(y):
        if grid[i][j][k] == 'L':
          lava += check_neighbor((i, j, k), grid, 'L')
  print(lava)

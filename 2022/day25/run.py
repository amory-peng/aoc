def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


map1 = {
  '2': 2,
  '1': 1,
  '0': 0,
  '-': -1,
  '=': -2
}

map2 = {
  2: '2',
  1: '1',
  0: '0',
  -1: '-',
  -2: '='
}


def snafu_to_int(snafu):
  n = len(snafu)
  res = 0
  for i in range(n - 1, -1, -1):
    c = snafu[i]
    res += map1[c] * 5 ** (n - i - 1)
  return res


def int_to_snafu(int):
  if int in map2:
    return map2[int]
  r = int % 5
  d = int // 5
  if r > 2:
    diff = 5 - r
    d += 1
    r = -diff
  return int_to_snafu(d) + int_to_snafu(r)


def part1(file):
  res = 0
  snafus = []
  for line in open(file).readlines():
    snafus.append([c for c in line.strip()])
  res = 0
  for snafu in snafus:
    i = snafu_to_int(snafu)
    res += i
  print(int_to_snafu(res))


def part2(file):
  res = 0
  for line in open(file).readlines():
    next
  print(res)

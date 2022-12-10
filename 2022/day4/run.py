def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):
  res = 0
  for line in open(file).readlines():
    line = line.strip()
    intervals = [[int(c) for c in sub.split('-')] for sub in line.split(',')]
    intervals.sort(key=lambda x: (x[1], -x[0]))
    (a0, _), (b0, _) = intervals
    if b0 <= a0:
      res += 1

  print(res)


def part2(file):
  res = 0
  for line in open(file).readlines():
    intervals = [[int(c) for c in sub.split('-')] for sub in line.split(',')]
    intervals.sort(key=lambda x: (x[1], -x[0]))
    (_, a1), (b0, _) = intervals
    if b0 <= a1:
      res += 1
  print(res)

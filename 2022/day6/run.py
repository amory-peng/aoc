def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):
  res = 0
  for line in open(file).readlines():
    for i in range(4, len(line)):
      sub = line[i - 4:i]
      if len(sub) == len(set(sub)):
        print(i)
        break


def part2(file):
  res = 0
  for line in open(file).readlines():
    for i in range(14, len(line)):
      sub = line[i - 14:i]
      if len(sub) == len(set(sub)):
        print(i)
        break

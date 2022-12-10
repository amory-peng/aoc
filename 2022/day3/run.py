def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def priority(c):
  res = ord(c)
  if c.isupper():
    res += 27 - ord('A')
  else:
    res += 1 - ord('a')
  return res


def part1(file):
  res = 0
  for line in open(file).readlines():
    curr = 0
    line = line.strip()
    n = len(line) // 2
    p1 = set(line[:n])
    p2 = set(line[n:])
    overlap = p1.intersection(p2)
    for c in overlap:
      curr += priority(c)
    res += curr
  print(res)


def part2(file):
  counter = 0
  bags = []
  res = 0
  for line in open(file).readlines():
    line = line.strip()
    counter += 1
    bags.append(set(line))
    if counter == 3:
      curr = 0
      overlap = bags[0]
      for bag in bags[1:]:
        overlap = overlap.intersection(bag)

      for c in overlap:
        curr += priority(c)
      res += curr
      bags = []
      counter = 0
  print(res)

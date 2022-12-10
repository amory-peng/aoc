from math import dist


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):
  res = 0
  seen = set()
  head = (0, 0)
  tail = (0, 0)
  delta = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
  }
  seen.add(tail)
  for line in open(file).readlines():
    direction, num_steps = line.strip().split()

    di, dj = delta[direction]
    for _ in range(int(num_steps)):
      i, j = head
      new_head = (i + di, j + dj)
      if dist(tail, new_head) >= 2:
        tail = head
      seen.add(tail)
      head = new_head

  print(len(seen))

# tail moves closer to head


def move_towards(head, tail):
  if dist(head, tail) < 2:
    return tail

  hi, hj = head
  ti, tj = tail
  if hi > ti:
    ti += 1
  elif hi < ti:
    ti -= 1
  if hj > tj:
    tj += 1
  elif hj < tj:
    tj -= 1

  return (ti, tj)


def part2(file):
  res = 0
  for line in open(file).readlines():
    res = 0
  seen = set()
  knots = [(0, 0) for _ in range(10)]
  delta = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
  }
  seen.add((0, 0))
  for line in open(file).readlines():
    direction, num_steps = line.strip().split()
    di, dj = delta[direction]
    for _ in range(int(num_steps)):
      # update the first knot
      di, dj = delta[direction]
      i, j = knots[0]
      knots[0] = (i + di, j + dj)
      # move rest of knots accordingly
      for i in range(1, 10):
        knots[i] = move_towards(knots[i - 1], knots[i])
      seen.add(knots[-1])

  print(len(seen))

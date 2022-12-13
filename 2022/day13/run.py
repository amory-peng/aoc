from functools import cmp_to_key


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def compare(left, right):
  left = [c for c in left]
  right = [c for c in right]
  while left and right:
    l = left.pop(0)
    r = right.pop(0)
    # both ints
    if isinstance(l, int) and isinstance(r, int):
      if not l == r:
        return -1 if l > r else 1
    # 1+ are lists, make sure both are lists and compare
    else:
      if isinstance(l, int):
        l = [l]
      if isinstance(r, int):
        r = [r]
      recurse = compare(l, r)
      if recurse:
        return recurse
  # empty list check
  if not left and right:
    return 1
  if left and not right:
    return -1
  # unable to determine
  return 0


def part1(file):
  res = 0
  data = open(file)
  counter = 1
  ans = 0
  while True:
    s1 = eval(data.readline())
    s2 = eval(data.readline())
    if compare(s1, s2) == 1:
      ans += counter
    counter += 1
    if not data.readline():
      break
  print(ans)


def part2(file):
  p1 = [[2]]
  p2 = [[6]]
  arr = [p1, p2]

  for line in open(file).readlines():
    line = line.strip()
    if line:
      arr.append(eval(line))
  arr = sorted(arr, key=cmp_to_key(compare), reverse=True)
  i1 = arr.index(p1) + 1
  i2 = arr.index(p2) + 1
  print(i1 * i2)

def run(file):
  print('part1: ')
  res1 = part1(file)
  print('part2: ')
  res2 = part2(file)


def get_diff(num, n):
  if num >= 0:
    return num % n
  num = -num
  num = num % n
  if num == 0:
    return 0
  return n - num


def calc(arr):
  n = len(arr)
  i = arr.index(0)
  print("0", i)
  print(arr[i:i + 10])
  res = 0
  for j in [1000, 2000, 3000]:
    num = (i + j) % n
    print(j, arr[num])
    res += arr[num]
  return res


def get_pos_of_tuple(turn, arr):
  for i, (order, num) in enumerate(arr):
    if turn == order:
      return (i, (order, num))


def part1(file):
  res = 0
  arr = []
  for line in open(file).readlines():
    arr.append(int(line.strip()))
  n = len(arr)

  #(order, num)
  arr = list(enumerate(arr))
  for turn in range(n):
    i, t = get_pos_of_tuple(turn, arr)
    (_, num) = t
    arr.pop(i)
    j = (i + num) % (n - 1)
    arr.insert(j, t)
  print(calc([c for _, c in arr]))


def part2(file):
  res = 0
  arr = []
  for line in open(file).readlines():
    arr.append(int(line.strip()) * 811589153)
  n = len(arr)

  #(order, num)
  arr = list(enumerate(arr))
  for _ in range(10):
    for turn in range(n):
      i, t = get_pos_of_tuple(turn, arr)
      (_, num) = t
      arr.pop(i)
      j = (i + num) % (n - 1)
      arr.insert(j, t)
  print(calc([c for _, c in arr]))

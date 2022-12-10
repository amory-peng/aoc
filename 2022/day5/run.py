from collections import defaultdict, deque


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):
  res = ""
  stacks = defaultdict(deque)
  for line in open(file).readlines():
    if "[" in line:
      for i in range(0, len(line), 4):
        c = line[i + 1]
        if not c.strip():
          continue
        stacks[i // 4 + 1].append(c)
    elif "move" in line:
      line = line.split(' ')
      move = int(line[1])
      start = int(line[3])
      end = int(line[5])
      for _ in range(move):
        stacks[end].appendleft(stacks[start].popleft())

  for key in sorted(stacks.keys()):
    res += stacks[key][0]
  print(res)


def part2(file):
  res = ""
  stacks = defaultdict(list)
  for line in open(file).readlines():
    if "[" in line:
      for i in range(0, len(line), 4):
        c = line[i + 1]
        if not c.strip():
          continue
        stacks[i // 4 + 1].append(c)
    elif "move" in line:
      line = line.split(' ')
      move = int(line[1])
      start = int(line[3])
      end = int(line[5])

      to_move = stacks[start][:move]
      stacks[start] = stacks[start][move:]
      stacks[end] = to_move + stacks[end]

  for key in sorted(stacks.keys()):
    res += stacks[key][0]
  print(res)

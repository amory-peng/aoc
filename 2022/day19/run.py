from functools import lru_cache
from collections import deque


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def parse(line):
  lines = line.strip().split('.')

  def helper(line):
    arr = line.split()
    i = arr.index("costs")
    arr = arr[i + 1:]
    cost = []
    for i, mat in enumerate(('ore', 'clay', 'obsidian')):
      try:
        cost.append(int(arr[arr.index(mat) - 1]))
      except:
        cost.append(0)
    cost.append(0)  # geode
    return tuple(cost)

  return {
      "ore": helper(lines[0]),
      "clay": helper(lines[1]),
      "obsidian": helper(lines[2]),
      "geode": helper(lines[3])
  }


def can_afford(stash, costs, type):
  cost = costs[type]
  for i in range(len(cost)):
    if stash[i] < cost[i]:
      return False
  new_stash = [stash[i] - cost[i] for i in range(len(stash))]
  return tuple(new_stash)


def part1(file):
  res = 0
  costs = {}
  id = 1
  for line in open(file).readlines():
    costs = parse(line)

    time = 24
    n = 4
    # optimization: stop making ore and clay robots if we have enough to make an obisidian
    # and geode robot every turn
    max_ore = costs['ore'][0] + costs['clay'][0] + \
        costs['obsidian'][0] + costs['geode'][0]
    max_clay = costs['obsidian'][1]
    max_obsidian = costs['geode'][2]
    types = ['ore', 'clay', 'obsidian', 'geode']

    # robots, stash
    queue = [((1, 0, 0, 0), (0, 0, 0, 0))]
    time = 0
    seen = set()
    best_states = []

    while time < 24:

      new_queue = []
      for state in queue:
        robots, stash = state
        if (robots, stash) in seen:
          continue

        seen.add(state)

        # add to stash with curr robots
        new_stash = tuple([robots[i] + stash[i] for i in range(n)])
        # no additional robot state
        new_queue.append((robots, new_stash))
        # for every robot, try to build and view state.
        # optimization: if we have enough robots to make a geode robot every turn, always do that
        for i in range(n):
          if i == 0 and robots[0] == max_ore:
            continue
          elif i == 1 and robots[i] == max_clay:
            continue
          elif i == 2 and robots[i] == max_obsidian:
            continue
          elif sub_stash := can_afford(stash, costs, types[i]):
            new_stash = [sub_stash[i] + robots[i] for i in range(n)]
            new_robots = [robots[j] + 1 if j == i else robots[j]
                          for j in range(n)]
            new_queue.append((tuple(new_robots), tuple(new_stash)))
      # optimization: at some point, we'll only want the ones with high geode count or high geode mininig robots
      pri_geode = sorted(new_queue, key=lambda x: (
        x[1][3], x[1][2], x[1][1], x[1][0]), reverse=True)
      pri_robot = sorted(new_queue, key=lambda x: (
        x[0][3], x[0][2], x[0][1], x[0][0]), reverse=True)
      queue = pri_geode[:1000] + pri_robot[:1000]
      time += 1
    max = queue[0][1][3]
    res += id * max
    id += 1
  print(res)


def part2(file):
  res = 1
  costs = {}
  id = 1
  for line in open(file).readlines():
    costs = parse(line)

    time = 24
    n = 4
    # optimization: stop making ore and clay robots if we have enough to make an obisidian
    # and geode robot every turn
    max_ore = costs['ore'][0] + costs['clay'][0] + \
        costs['obsidian'][0] + costs['geode'][0]
    max_clay = costs['obsidian'][1]
    max_obsidian = costs['geode'][2]
    types = ['ore', 'clay', 'obsidian', 'geode']

    # robots, stash
    queue = [((1, 0, 0, 0), (0, 0, 0, 0))]
    time = 0
    seen = set()
    best_states = []

    while time < 32:
      new_queue = []
      for state in queue:
        robots, stash = state
        if (robots, stash) in seen:
          continue

        seen.add(state)

        # add to stash with curr robots
        new_stash = tuple([robots[i] + stash[i] for i in range(n)])
        # no additional robot state
        new_queue.append((robots, new_stash))
        # for every robot, try to build and view state.
        # optimization: if we have enough robots to make a geode robot every turn, always do that
        for i in range(n):
          if i == 0 and robots[0] == max_ore:
            continue
          elif i == 1 and robots[i] == max_clay:
            continue
          elif i == 2 and robots[i] == max_obsidian:
            continue
          elif sub_stash := can_afford(stash, costs, types[i]):
            new_stash = [sub_stash[i] + robots[i] for i in range(n)]
            new_robots = [robots[j] + 1 if j == i else robots[j]
                          for j in range(n)]
            new_queue.append((tuple(new_robots), tuple(new_stash)))
      # optimization: at some point, we'll only want the ones with high geode count or high geode mininig robots
      pri_geode = sorted(new_queue, key=lambda x: (
        x[1][3], x[1][2], x[1][1], x[1][0]), reverse=True)
      pri_robot = sorted(new_queue, key=lambda x: (
        x[0][3], x[0][2], x[0][1], x[0][0]), reverse=True)
      queue = pri_geode[:1000] + pri_robot[:1000]
      time += 1
      # print("id: ", id, "time: ", time, "queue len:", len(queue))
    max = queue[0][1][3]
    print('id: ', id, "geodes:", max)
    res *= max
    id += 1
    if id == 4:
      break
  print(res)

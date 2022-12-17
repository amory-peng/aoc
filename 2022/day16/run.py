from functools import lru_cache
from collections import defaultdict, deque


def run(file):
  # print('part1: ')
  # part1(file)
  print('part2: ')
  part2(file)


def parse_line(line):
  fr, tns = line.strip().split(';')
  fr = fr.split()
  label = fr[1]
  fr = int(fr[-1].replace("rate=", ""))
  tns = tns.split()[4:]
  tns = [tn.replace(',', '') for tn in tns]
  return (label, fr, tns)


def make_adj(data):
  map = {}
  for (label, fr, tns) in data:
    map[label] = (fr, tns)
  return map


def part1(file):
  res = 0
  data = []
  for line in open(file).readlines():
    data.append(parse_line(line))

  valves, flow, dist, adj = [], {}, {}, {}

  for valve, fr, ne in data:
    flow[valve] = fr
    adj[valve] = ne
    valves.append(valve)
  n = len(valves)

  def bfs(start, stop, seen):
    queue = [start]
    res = 0
    while queue:
      new_queue = []
      for valve in queue:
        if valve == stop:
          return res
        seen.add(valve)
        for ne in adj[valve]:
          if ne not in seen:
            new_queue.append(ne)
      res += 1
      queue = new_queue

  for i in range(n):
    vi = valves[i]
    if not vi == 'AA' and flow[vi] == 0:
      continue
    for j in range(n):
      vj = valves[j]
      di = dist.get(vi, {})
      # dont care about valves with 0 fr or self
      if not i == j and flow[vj] > 0:
        di[vj] = bfs(vi, vj, set())

      dist[vi] = di

  @lru_cache
  def search(time, curr_valve, unopened):

    opened = 0
    for (ne, d) in dist[curr_valve].items():
      if ne in unopened and time - d - 1 >= 0:
        opened = max(
          search(time - d - 1, ne, unopened - {curr_valve}), opened)
    opened += flow[curr_valve] * time
    return opened

  print(search(30, "AA", frozenset(valves) - {'AA'}))


def part2(file):
  res = 0
  data = []
  for line in open(file).readlines():
    data.append(parse_line(line))

  valves, flow, dist, adj = [], {}, {}, {}

  for valve, fr, ne in data:
    flow[valve] = fr
    adj[valve] = ne
    valves.append(valve)
  n = len(valves)

  def bfs(start, stop, seen):
    queue = [start]
    res = 0
    while queue:
      new_queue = []
      for valve in queue:
        if valve == stop:
          return res
        seen.add(valve)
        for ne in adj[valve]:
          if ne not in seen:
            new_queue.append(ne)
      res += 1
      queue = new_queue

  for i in range(n):
    vi = valves[i]
    if not vi == 'AA' and flow[vi] == 0:
      continue
    for j in range(n):
      vj = valves[j]
      di = dist.get(vi, {})
      # dont care about valves with 0 fr or self
      if not i == j and flow[vj] > 0:
        di[vj] = bfs(vi, vj, set())

      dist[vi] = di

  paths = defaultdict(lambda: -1)
  queue = deque([(26, 0, 'AA', frozenset({'AA'}))])

  while queue:
    time, total_flow, curr_valve, path = queue.popleft()
    total_flow += flow[curr_valve] * time
    if total_flow > paths[path]:
      paths[path] = total_flow

    for (ne, d) in dist[curr_valve].items():
      if ne not in path and time - d - 1 >= 0:
        queue.append((time - d - 1, total_flow, ne, path | {ne}))

  res = 0
  for path1 in paths:
    for path2 in paths:
      if path1 & path2 == {'AA'}:
        # print(path1, path2, paths[path1] + paths[path2])
        res = max(paths[path1] + paths[path2], res)
  print(res)

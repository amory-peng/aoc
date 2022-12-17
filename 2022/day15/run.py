def run(file):
  # print('part1: ')
  # part1(file)
  print('part2: ')
  part2(file)


def parse(line):
  res = []
  for str in line.split(':'):
    xeq = str.find("=")
    comma = str.find(",")
    x = str[xeq + 1: comma]
    str = str[comma:]
    yeq = str.find("=")
    y = str[yeq + 1:]
    res.append((int(x), int(y)))
  return res


def dist(pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2
  return abs(x1 - x2) + abs(y1 - y2)

# [x, [y interval covered]]


def radius(pos, d):
  res = set()
  x, y = pos
  for dx, i in enumerate(range(x, x + d + 1)):
    int = (y + d - dx, y - d + dx)
    for j in int:
      res.add((i, j))

  for dx, i in enumerate(range(x, x - d - 1, -1)):
    int = (y + d - dx, y - d + dx)
    for j in int:
      res.add((i, j))
  # for i in range(y - d, y + d + 1):
  #   line = ""
  #   for j in range(x - d, x + d + 1):
  #     if (j, i) in res:
  #       line += '#'
  #     else:
  #       line += '.'
  #   print(line)

  return res


def part1(file):
  sensors = []
  beacons = []
  for line in open(file).readlines():
    sensor, beacon = parse(line)
    sensors.append(sensor)
    beacons.append(beacon)
  sorted_coords = sorted(sensors + beacons)

  min_x = sorted_coords[0][0]
  max_x = sorted_coords[-1][0]
  min_dists = [dist(sensors[i], beacons[i]) for i in range(len(sensors))]
  max_dist = max(min_dists) + 1
  beacons = set(beacons)
  res = 0
  for x in range(min_x - max_dist, max_x + max_dist):
    pos = (x, 2000000)
    cannot_exist = False
    if pos in beacons:
      continue
    # this pos cannot be shortest dist for any beacon
    for i, sensor in enumerate(sensors):
      if dist(pos, sensor) <= min_dists[i]:
        cannot_exist = True
        break
    if cannot_exist:
      res += 1
  print("ans", res)


def part2(file):
  sensors = []
  beacons = []
  for line in open(file).readlines():
    sensor, beacon = parse(line)
    sensors.append(sensor)
    beacons.append(beacon)
  min_dists = [dist(sensors[i], beacons[i]) for i in range(len(sensors))]
  lim = 4000000
  covered = False
  for i, sensor in enumerate(sensors):
    potential_empty_points = radius(sensor, min_dists[i] + 1)
    print(len(potential_empty_points))
    print("checking sensor", i)
    for point in potential_empty_points:
      if not (0 <= point[0] <= lim and 0 <= point[1] <= lim):
        continue
      covered = False
      for j, rest in enumerate(sensors):
        if dist(point, rest) <= min_dists[j]:
          # print("point", point, "covered by", j)
          covered = True
          break
      if not covered:
        print("beacon location: ", point)
        print(point[0] * 4000000 + point[1])
        return

  print("something went wrong")

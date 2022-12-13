from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional, Dict
from math import inf


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


@dataclass
class Directory:
  name: str
  parent: Optional["Directory"]
  files: Dict[str, int] = field(default_factory=lambda: {})
  directories: Dict[str, "Directory"] = field(
    default_factory=lambda: {})


def part1(file):
  root = Directory(name="root", parent=None)

  def get_directories(name, parent=None):
    if not parent:
      return root
    if name not in parent.directories:
      parent.directories[name] = Directory(name=name, parent=parent)

    return parent.directories[name]

  curr = None
  for line in open(file).readlines():
    line = line.strip()
    if "$ cd" in line:
      if ".." in line:
        curr = curr.parent if curr.parent else get_directories('root')
      else:
        curr = get_directories(line[5:], curr)
    # the only time this is true is when we're ls'ing the curr directory
    elif line[0] != "$":
      if "dir " in line:
        _, dir = line.split()
        curr.directories[dir] = (get_directories(dir, curr))
      else:
        size, filename = line.split()
        curr.files[filename] = int(size)

  def get_sizes(dir, memo, path):
    key = f"{path}{dir.name}"
    # print(key)
    if key in memo:
      return memo[key]

    size = 0
    for filesize in dir.files.values():
      size += filesize

    for child_dir in dir.directories.values():
      size += get_sizes(child_dir, memo, path + f"{dir.name}/")

    memo[key] = size
    return size

  memo = {}
  get_sizes(get_directories('/'), memo, "")

  res = 0
  for val in memo.values():
    if val <= 100000:
      res += val
  print(res)
  return [root, memo]


def part2(file):
  root, memo = part1(file)
  res = inf
  curr_space = memo["root"]
  for (file, size) in memo.items():
    unused_space = 70000000 - curr_space + size
    if unused_space >= 30000000:
      res = min(res, size)
  print(res)

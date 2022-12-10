from dataclasses import dataclass


@dataclass
class Rock:
  id = 'A'
  beats = "C"
  loses = "B"
  score = 1


@dataclass
class Paper:
  id = 'B'
  beats = "A"
  loses = "C"
  score = 2


@dataclass
class Scissor:
  id = 'C'
  beats = "B"
  loses = 'A'
  score = 3


def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)


def part1(file):
  map = {
    # rock
    'A': 1,
    'X': 1,
    # paper
    'B': 2,
    'Y': 2,
    # scissors
    'C': 3,
    'Z': 3
  }

  score = 0
  for line in open(file).readlines():
    p1, p2 = [map[p] for p in line.split()]
    score += p2
    # tie
    if p1 == p2:
      score += 3
    # win scenarios
    elif (
      p1 == 1 and p2 == 2 or
      p1 == 2 and p2 == 3 or
      p1 == 3 and p2 == 1
    ):
      score += 6

  print(score)


def part2(file):
  map = {
    # rock
    'A': Rock(),
    'X': 0,
    # paper
    'B': Paper(),
    'Y': 3,
    # scissors
    'C': Scissor(),
    'Z': 6
  }
  score = 0
  for line in open(file).readlines():
    p1, outcome = line.split()
    p1 = map[p1]
    score += map[outcome]
    # lose
    if outcome == 'X':
      score += map[p1.beats].score
    # draw
    elif outcome == 'Y':
      score += p1.score
    # win
    else:
      score += map[p1.loses].score
  print(score)

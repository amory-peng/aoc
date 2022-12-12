from collections import deque

def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)

class Monkey:
  inspected = 0
  items = []
  
  def parse_operation(self, operator, value): 
    if operator == "*":
      if value == "old":
        self.operation = lambda x: x * x
      else:
        self.operation = lambda x: x * int(value)
    else:
      self.operation = lambda x: x + int(value)

  def parse_test(self, divisor, true, false):
    self.divisor = divisor
    self.test = lambda x: true if x % divisor == 0 else false

  def play(self, divisor=1, common_multiple=1):
    # (item, monkey)
    res = []
    while self.items:
      item = self.items.popleft()
      item = self.operation(item) // divisor
      monkey = self.test(item)
      item = item % common_multiple
      self.inspected += 1
      res.append((item, monkey))
    return res
      

def part1(file):
  monkeys = []
  data = open(file)
  while (line := data.readline()):
    line = line.strip()
    if "Monkey" not in line:
      continue
    monkey = Monkey()
    items = data.readline()
    i = items.find(":")
    monkey.items = deque([int(c) for c in items[i+1:].split(',')])
    
    operation = data.readline()
    i = operation.find("old")
    operation = operation[i+4:].split()
    monkey.parse_operation(operation[0], operation[1])

    test = int(data.readline().split()[-1])
    condition_true = int(data.readline().split()[-1])
    condition_false = int(data.readline().split()[-1])
    monkey.parse_test(test, condition_true, condition_false)
    monkeys.append(monkey)

  for _ in range(20):
    for monkey in monkeys:
      updates = monkey.play(3)
      for (item, monkey) in updates:
        monkeys[monkey].items.append(item)

  bsns = [monkey.inspected for monkey in monkeys]
  print(sorted(bsns)[-1] * sorted(bsns)[-2])
  
def part2(file):
  monkeys = []
  data = open(file)
  while (line := data.readline()):
    line = line.strip()
    if "Monkey" not in line:
      continue
    monkey = Monkey()
    items = data.readline()
    i = items.find(":")
    monkey.items = deque([int(c) for c in items[i+1:].split(',')])
    
    operation = data.readline()
    i = operation.find("old")
    operation = operation[i+4:].split()
    monkey.parse_operation(operation[0], operation[1])

    test = int(data.readline().split()[-1])
    condition_true = int(data.readline().split()[-1])
    condition_false = int(data.readline().split()[-1])
    monkey.parse_test(test, condition_true, condition_false)
    monkeys.append(monkey)
  common_multiple = 1
  for monkey in monkeys:
    common_multiple *= monkey.divisor 

  print(common_multiple)
  for round in range(10000):
    if round % 1000 == 0 or round == 1:
      print([monkey.inspected for monkey in monkeys])
    for monkey in monkeys:
      updates = monkey.play(1, common_multiple)
      for (item, monkey) in updates:
        monkeys[monkey].items.append(item)

  bsns = [monkey.inspected for monkey in monkeys]
  print(sorted(bsns)[-1] * sorted(bsns)[-2])

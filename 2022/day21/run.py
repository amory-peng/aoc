import operator


def run(file):
  # print('part1: ')
  # part1(file)
  print('part2: ')
  part2(file)


ops = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.floordiv
}


def parse(line):
  monkey, operation = line.strip().split(': ')
  try:
    num = int(operation)
    return (monkey, num)
  except:
    for key in ops.keys():
      if key in line:
        a, b = operation.split(f' {key} ')
        return (monkey, (key, a, b))


def part1(file):

  monkeys = {}
  for line in open(file).readlines():
    monkey, operation = parse(line)
    monkeys[monkey] = operation

  def recurse(monkey):
    op = monkeys[monkey]
    if type(op) is int:
      return ops
    key, a, b = op
    return ops[key](recurse(a), recurse(b))
  print(recurse('root'))


def part2(file):
  monkeys = {}
  for line in open(file).readlines():
    monkey, operation = parse(line)
    monkeys[monkey] = operation
  # returns an array of [numerator, denominator], where both num and denom
  # is of array [x^0, x^1, x^2...]

  def multiply(a, b):
    num_a, denom_a = a
    num_b, denom_b = b
    num = []
    denom = []
    if denom_a == [1] and denom_b == [1]:
      arr = [0 for _ in range(len(num_a) + len(num_b) - 1)]
      for i, mag_a in enumerate(num_a):
        for j, mag_b in enumerate(num_b):
          arr[i + j] += mag_a * mag_b
      num = arr
      denom = [1]
      return [num, denom]
    else:
      num = multiply([num_a, [1]], [num_b, [1]])[0]
      denom = multiply([denom_a, [1]], [denom_b, [1]])[0]
    if num == denom:
      num = denom = [1]
    return [num, denom]

  def divide(a, b):
    num_b, denom_b = b
    b = [denom_b, num_b]
    return multiply(a, b)

  def add(a, b):
    num_a, denom_a = a
    num_b, denom_b = b

    n_a = multiply([num_a, [1]], [denom_b, [1]])[0]
    n_b = multiply([num_b, [1]], [denom_a, [1]])[0]
    d = multiply([denom_a, [1]], [denom_b, [1]])[0]
    arr = [0 for _ in range(max(len(n_a), len(n_b)))]
    for i in range(max(len(n_a), len(n_b))):
      mag_a = n_a[i] if i < len(n_a) else 0
      mag_b = n_b[i] if i < len(n_b) else 0
      arr[i] += mag_a + mag_b
    return [arr, d]

  def sub(a, b):
    num_a, denom_a = a
    num_b, denom_b = b

    n_a = multiply([num_a, [1]], [denom_b, [1]])[0]
    n_b = multiply([num_b, [1]], [denom_a, [1]])[0]
    d = multiply([denom_a, [1]], [denom_b, [1]])[0]
    arr = [0 for _ in range(max(len(n_a), len(n_b)))]
    for i in range(max(len(n_a), len(n_b))):
      mag_a = n_a[i] if i < len(n_a) else 0
      mag_b = n_b[i] if i < len(n_b) else 0
      arr[i] += mag_a - mag_b
    return [arr, d]

  ops2 = {
      '+': add,
      '-': sub,
      '*': multiply,
      '/': divide
    }

  def recurse(monkey):
    if monkey == 'humn':
      return [[0, 1], [1]]
    op = monkeys[monkey]
    if type(op) is int:
      num = [op]
      denom = [1]
      return [num, denom]
    key, a, b = op
    return ops2[key](recurse(a), recurse(b))

  monk1 = monkeys['root'][1]
  monk2 = monkeys['root'][2]
  # print(recurse('root'))
  print(recurse(monk1))
  print(recurse(monk2))

def run(file):
  print('part1: ')
  part1(file)
  print('part2: ')
  part2(file)

def part1(file):
    cycle = 1
    x = 1
    addx = None
    file = open(file)
    res = 0
    while(True):
        if (cycle - 20) % 40 == 0:
            print("cycle:", cycle, "x:", x)
            print("signal str: ", cycle * x)
            res += cycle * x
        # something cached, increase x and cycle
        if addx:
            x += addx
            addx = None
        # nothing cached, look for a command    
        else:
            line = file.readline().strip()
            # no command found, break
            if not line: 
                break
            # noop, do nothing but increment cycle
            if line != "noop":
                addx = int(line.split()[1])
        cycle += 1
    print(res)
        
def part2(file):
    
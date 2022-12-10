from math import inf
import heapq


def run(file):
    part1(file)
    part2(file)


def part1(file):
    res = -inf
    curr = 0
    for line in open(file).readlines():
        # print(line)
        if line == "\n":
            res = max(curr, res)
            curr = 0
        else:
            curr += int(line)
    res = max(curr, res)
    print(res)


def part2(file):
    arr = []
    curr = 0
    for line in open(file).readlines():
        # print(line)
        if line == "\n":
            arr.append(curr)
            curr = 0
        else:
            curr += int(line)
    arr.append(curr)
    arr.sort(reverse=True)
    print(sum(arr[:3]))

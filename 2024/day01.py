import sys

list1, list2 = zip(*[(tmp := line.rstrip().split(), (int(tmp[0]), int(tmp[1])))[1] for line in sys.stdin.readlines()])

list1 = sorted(list1)
list2 = sorted(list2)

diff = sum([max(x) - min(x) for x in zip(list1, list2)])
print(f"Part 1: {diff}")

score = sum([x * list2.count(x) for x in list1])
print(f"Part 2: {score}")

import sys
from functools import reduce
from itertools import combinations

reports = [(tmp := line.split(), [int(x) for x in tmp])[1] for line in sys.stdin.readlines()]

def safe(report) :
  deltas = zip(report[:-1], report[1:])
  progressions = [tup[1] - tup[0] for tup in deltas]
  return all([x in range(1, 4) for x in progressions]) or all([x in range(-3, 0) for x in progressions])

part1_safe = [safe(row) for row in reports].count(True)

print(f"Part 1: {part1_safe}")

# My initial thought was that we should do an "all-but-one" check on the progressions. All is good if at most one progression is False.
# But removal of a bad level actually changes *two* progressions. We have to model the removal of levels rather than the removal of progressions.

def safe2(report) :
  return safe(report) or any([safe(x) for x in combinations(report, len(report) - 1)])

part2_safe = [safe2(row) for row in reports].count(True)
print(f"Part 2: {part2_safe}")


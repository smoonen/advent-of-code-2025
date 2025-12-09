import sys
from functools import cmp_to_key

rules, updates = "".join(sys.stdin.readlines()).split("\n\n")
rules = [(int(x), int(y)) for x, y in [line.split("|") for line in rules.split("\n")]]
updates = [[int(x) for x in line.split(",")] for line in updates.rstrip().split("\n")]

valid = lambda u : all([u.index(r[0]) < u.index(r[1]) for r in rules if u.count(r[0]) and u.count(r[1])])
mid = lambda u : u[len(u) >> 1]

# Sum middle numbers of valid updates
total = sum([mid(u) for u in updates if valid(u)])
print(f"Part 1: {total}")

def cmp(p1, p2) :
  if rules.count((p1, p2)) == 0 and rules.count((p2, p1)) == 0 : # No rule; sort either way
    return 0
  elif rules.count((p1, p2)) == 0 : # They are in correct order
    return -1
  return 1

total = sum([mid(sorted(u, key = cmp_to_key(cmp))) for u in updates if not valid(u)])
print(f"Part 2: {total}")


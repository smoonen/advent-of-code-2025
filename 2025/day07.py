import sys
# Only in v3.10 and higher
#from itertools import pairwise

Splits = 0

def advance(r1, r2) :
  global Splits, Timelines

  next_timelines = [0 for x in Timelines]
  for ix, c1 in enumerate(r1) :
    if c1 in ('S', '|') :
      if r2[ix] == '^' : # Fortunately we don't need to handle edge cases nor are there adjacent splitters
        r2[ix - 1] = r2[ix + 1] = '|'
        Splits += 1
        next_timelines[ix - 1] += Timelines[ix]
        next_timelines[ix + 1] += Timelines[ix]
      else :
        r2[ix] = '|'
        next_timelines[ix] += Timelines[ix]
  Timelines = next_timelines

rows = [list(line.rstrip()) for line in sys.stdin.readlines()]

Timelines = [int(x == 'S') for x in rows[0]]

# If you have v3.10 or greater
#[advance(p1, p2) for p1, p2 in pairwise(rows)]

for x in range(len(rows) - 1) :
  advance(rows[x], rows[x+1])

print(f"Part 1: {Splits}")

print(f"Part 2: {sum(Timelines)}")


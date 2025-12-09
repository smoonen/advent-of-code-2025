import itertools, sys, numpy
# Only in v3.10 and higher
#from itertools import pairwise

RED = ord('R')
GREEN = ord('G')

def pairwise(i) :
  iterator = iter(i)
  a = next(iterator)
  for b in iterator :
    yield a,b
    a = b
area = lambda p1, p2 : (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
normalize = lambda x, y: (int(x / x) if x != 0 else 0, int(y / y) if y != 0 else 0)

coords = [(int(x), int(y)) for x, y in [line.rstrip().split(',') for line in sys.stdin.readlines()]]

best = max([area(p1, p2) for p1, p2 in itertools.combinations(coords, 2)])

print(f"Part 1: {best}")

max_x = max([pt[0] for pt in coords]) + 1
max_y = max([pt[1] for pt in coords]) + 1
tiles = numpy.zeros((max_x, max_y), numpy.int8)

# Draw lines. Remember an interior point.
lastdirection = None
interior = None
for pair in pairwise(coords + [coords[0]]) :
  tiles[pair[0][0]][pair[0][1]] = RED
  tiles[pair[1][0]][pair[1][1]] = RED
  for x in range(min(pair[0][0], pair[1][0]) + 1, max(pair[0][0], pair[1][0])) :
    for y in range(min(pair[0][1], pair[1][1]) + 1, max(pair[0][1], pair[1][1])) :
      tiles[x][y] = GREEN
  if interior is None :
    # Normalize the direction so that it is something like (-1,0) instead of (-55,0)
    curdirection = normalize(pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
    if lastdirection is None :
      lastdirection = curdirection
    else :
      # Undo last direction and apply current direction to our first point. This will give us an interior point.
      interior = (pair[0][0] - lastdirection[0] + curdirection[0], pair[0][1] - lastdirection[1] + curdirection[1])

queue = set((interior,))
while queue :
  stalequeue = queue
  queue = set()
  for x, y in stalequeue :
    tiles[x][y] = GREEN
  for x, y in stalequeue :
    [queue.add((x + dx, y + dy)) for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)) if tiles[x+dx][y+dy] == 0]


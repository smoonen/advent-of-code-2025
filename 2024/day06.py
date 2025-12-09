import copy, sys

matrix = [list(line.rstrip()) for line in sys.stdin.readlines()]

valid = lambda x, y : x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0])

ObstructionCandidates = set()

def walk(matrix) :
  global ObstructionCandidates

  locations = set()

  # Locate the turtle and initialize his direction
  direction = (-1, 0)
  x = [line.count('^') for line in matrix].index(1)
  y = matrix[x].index('^')

  while True :
    if (x, y, direction) in locations : # We've been here before - and pointed in the same direction
      raise RecursionError
    else :
      locations.add((x, y, direction))
      matrix[x][y] = 'X'

    while valid(x + direction[0], y + direction[1]) : # Look ahead for obstruction; loop as we may need to turn multiple times
      if matrix[x + direction[0]][y + direction[1]] in ('#', 'O') : # Actually obstructed
        direction = (direction[1], -direction[0]) # Turn right
      else : # Not obstructed so it is a candidate location for a future obstruction
        ObstructionCandidates.add((x + direction[0], y + direction[1]))
        break

    x, y = (x + direction[0], y + direction[1])
    if not valid(x, y) :
      break

  return matrix

m1 = walk(copy.deepcopy(matrix))
total = sum([line.count('X') for line in m1])
print(f"Part 1: {total}")

# Experiment with obstructions. Previously we kept track of obstruction candidate locations.
count = 0
for x, y in copy.copy(ObstructionCandidates) :
  if matrix[x][y] != '^' :
    m2 = copy.deepcopy(matrix)
    m2[x][y] = 'O'
    try : walk(m2)
    except : count += 1

print(f"Part 2: {count}")


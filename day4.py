import copy, sys

matrix = list([list(x.rstrip()) for x in sys.stdin.readlines()])

def neighborcount(x, y) :
  count = 0
  for tup in [(x,y) for x in range(-1,2) for y in range(-1,2) if x != 0 or y != 0] :
    count += (matrix[x + tup[0]][y + tup[1]] == '@') if x+tup[0] >= 0 and x+tup[0] < len(matrix) and y+tup[1] >= 0 and y+tup[1] < len(matrix[0]) else 0
  return count

def movablecount(destroy = False) :
  global matrix
  newmatrix = copy.deepcopy(matrix) if destroy else None
  count = 0
  for x in range(len(matrix)) :
    for y in range(len(matrix[x])) :
      if matrix[x][y] == '@' and neighborcount(x, y) < 4 :
        count += 1
        if destroy : newmatrix[x][y] = '.'
  if destroy : matrix = newmatrix
  return count

print(f"Part 1: {movablecount()}")

total = 0
while True :
  count = movablecount(True)
  if count : total += count
  else     : break

print(f"Part 2: {total}")


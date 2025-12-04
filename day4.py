import copy, sys

matrix = list([list(x.rstrip()) for x in sys.stdin.readlines()])

# Idea: we can simplify the exclusion ever so slightly if we allow the neighbor count to include the current cell.
# We simply adjust our expectation to be <5 instead of <4.

legal = lambda x, l : x >= 0 and x < len(l)
neighborcount = lambda x, y : sum([int(matrix[i][j] == '@') for i in (x-1,x,x+1) for j in (y-1,y,y+1) if legal(i, matrix) and legal(j, matrix[0])])

total = sum([int(neighborcount(x, y) < 5) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == '@'])
print(f"Part 1: {total}")

def movablecount(destroy = False) :
  global matrix
  newmatrix = copy.deepcopy(matrix) if destroy else None
  count = 0
  for x in range(len(matrix)) :
    for y in range(len(matrix[x])) :
      if matrix[x][y] == '@' and neighborcount(x, y) < 5 :
        count += 1
        if destroy : newmatrix[x][y] = '.'
  if destroy : matrix = newmatrix
  return count

total = 0
while True :
  count = movablecount(True)
  if count : total += count
  else     : break

print(f"Part 2: {total}")


import sys

matrix = [list(line.rstrip()) for line in sys.stdin.readlines()]

patterns = [list(zip(4*[0], range(4)))] + [list(zip(range(4), 4*[0]))] + [list(zip(range(4), range(4)))] + [list(zip(range(4), range(0,-4,-1)))]
patterns += [sorted(x, reverse=True) for x in patterns]

cell = lambda x, y : matrix[x][y] if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) else None
delta = lambda x, y, d : cell(x+d[0], y+d[1])
hunt = lambda x, y : sum([int(delta(x, y, p[0]) == 'X' and delta(x, y, p[1]) == 'M' and delta(x, y, p[2]) == 'A' and delta(x, y, p[3]) == 'S') for p in patterns])
total = sum([hunt(x, y) for x in range(len(matrix)) for y in range(len(matrix[0]))])

print(f"Part 1: {total}")

rot90 = lambda m : list(zip(*m[::-1]))
template = (('M.M'),('.A.'),('S.S'))
templates = [template]
for x in range(3) :
  templates.append(rot90(templates[-1]))

match = lambda x, y, template : all([cell(x+dx, y+dy) == template[dx][dy] for dx in range(3) for dy in range(3) if template[dx][dy] != '.'])
hunt = lambda x, y : any([match(x, y, t) for t in templates])
total = sum([hunt(x, y) for x in range(len(matrix)) for y in range(len(matrix[0]))])

print(f"Part 2: {total}")


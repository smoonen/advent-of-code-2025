import itertools, sys

matrix = [line.rstrip() for line in sys.stdin.readlines()]
frequencies = set([char for line in matrix for char in line if char != '.'])

valid = lambda x, y : x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0])
antennas = lambda char : [(x, y) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == char]

antinodes = set()
for freq in frequencies :
  for pair in itertools.permutations(antennas(freq), 2) :
    ant1 = (2 * pair[0][0] - pair[1][0], 2 * pair[0][1] - pair[1][1])
    ant2 = (2 * pair[1][0] - pair[0][0], 2 * pair[1][1] - pair[0][1])

    if valid(ant1[0], ant1[1]) : antinodes.add(ant1)
    if valid(ant2[0], ant2[1]) : antinodes.add(ant2)

print(f"Part 1: {len(antinodes)}")

antinodes = set()
for freq in frequencies :
  for pair in itertools.permutations(antennas(freq), 2) :
    d = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])

    tmp = pair[0]
    while valid(tmp[0], tmp[1]) :
      antinodes.add(tmp)
      tmp = tuple([x+y for x,y in zip(tmp, d)])
    tmp = pair[0]
    while valid(tmp[0], tmp[1]) :
      antinodes.add(tmp)
      tmp = tuple([x-y for x,y in zip(tmp, d)])

print(f"Part 2: {len(antinodes)}")


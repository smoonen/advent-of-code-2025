import math, sys

# Retrieve coordinates
coords = [(int(x), int(y), int(z)) for x, y, z in [line.rstrip().split(",") for line in sys.stdin.readlines()]]

# Create a coordinate map of circuit belonging to each coordinate
coordmap = dict(zip(coords, [-1] * len(coords)))
# Fashon a map of the pairs of distances, calculating distance between each pair
pairmap = [(math.dist(coords[i], coords[j]), coords[i], coords[j]) for i in range(len(coords)) for j in range(i+1, len(coords))]
# Sort distances
pairmap.sort(key = lambda x : x[0])

# Connect points and merge circuits
next_circuit_id = 0
step = 0
while True :
  p1, p2 = pairmap[step][1:]
  if coordmap[p1] == -1 and coordmap[p2] == -1 :
    coordmap[p1] = coordmap[p2] = next_circuit_id
    next_circuit_id += 1
  elif coordmap[p1] == -1 or coordmap[p2] == -1 :
    new_id = max(coordmap[p1], coordmap[p2])
    coordmap[p1] = coordmap[p2] = new_id
  elif coordmap[p1] != coordmap[p2] : # Swallow up lesser circuit with greater one
    old_id = min(coordmap[p1], coordmap[p2])
    new_id = max(coordmap[p1], coordmap[p2])
    for coord in coords :
      if coordmap[coord] == old_id :
        coordmap[coord] = new_id

  # List the circuit ids including duplicates
  circuitids = [c for c in coordmap.values() if c != -1]
  # Identify unique circuit ids
  circuits = list(set(circuitids))

  if step == 999 : # Part 1 complete
    # Create a map of circuit ids to circuit size
    circuitsize = [(c, circuitids.count(c)) for c in circuits]
    # Sort by size, descending
    circuitsize.sort(key = lambda x : -x[1])
    # Multiply three largest
    part1 = circuitsize[0][1] * circuitsize[1][1] * circuitsize[2][1]

    print(f"Part 1: {part1}")

  elif len(circuits) == 1 and -1 not in coordmap.values() : # Mission accomplished
    part2 = p1[0] * p2[0]
    print(f"Part 2: {part2}")
    break

  step += 1


import sys

edges = dict([(src, nxt.split(' ')) for src, nxt in [line.rstrip().split(": ") for line in sys.stdin.readlines()]])
edges["out"] = []

count = {}

# Sweep through maintaining a wavefront for a breadth first search
front = ['you']
while front :
  new_front = []
  for node in front :
    count[node] = count[node] + 1 if node in count else 1
    if node in edges :
      new_front.extend(edges[node])
  front = new_front

print(f"Part 1: {count['out']}")

# For part 2, build a list of immediate ancestors for each node.
# This will allow us to determine when a rollup is possible, if all ancestors have reported in.
# We will destroy this list as we go, as a way of keeping track of what is left.
ancestors = dict([(node, []) for node in edges.keys()])
for node, nextlist in edges.items() :
  for nxt in nextlist :
    ancestors[nxt].append(node)

# Now we rollup a counter for each node until we have one node left.
# We can rollup a node once its ancestors are complete.
# Each node is represented as a tuple counting:
#  - count of visits that haven't hit any milestones
#  - count of visits that hit DAC milestone
#  - count of visits that hit FFT milestone
#  - count of visits that hit both milestones
count = dict([(node, [0, 0, 0, 0]) for node in edges.keys()])

def rollup(node) :
  tail = []
  delta = count[node]

  if node == 'dac' :
    assert(delta[1] == 0)
    assert(delta[3] == 0)
    delta = [0, delta[0], 0, delta[2]]
  elif node == 'fft' :
    assert(delta[2] == 0)
    assert(delta[3] == 0)
    delta = [0, 0, delta[0], delta[1]]

  for child in edges[node] :
    count[child] = list(map(sum, zip(delta, count[child])))
    del ancestors[child][ancestors[child].index(node)]
    if not ancestors[child] : # We were the last ancestor; we can now roll up this child
      tail += [child]
  for child in tail :
    rollup(child)

count["svr"] = [1, 0, 0, 0]
rollup("svr")

print(f"Part 2: {count['out'][3]}")


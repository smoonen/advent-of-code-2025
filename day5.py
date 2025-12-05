import sys

ranges, items = "".join(sys.stdin.readlines()).rstrip().split("\n\n")
ranges = [(tmp := line.split("-"), range(int(tmp[0]), int(tmp[1])+1))[1] for line in ranges.split("\n")]
items = [int(x) for x in items.split("\n")]

fresh = sum([int(any([item in r for r in ranges])) for item in items])

print(f"Part 1: {fresh}")

# Sort ranges by their starting value
ranges.sort(key = lambda x : x.start)

# Combine ranges where possible. Short circuit if we have moved past the cursor's ending value
cursor = 0
while cursor < len(ranges) :
  while cursor + 1 < len(ranges) and ranges[cursor].stop >= ranges[cursor + 1].start :
    ranges[cursor] = range(ranges[cursor].start, max(ranges[cursor].stop, ranges[cursor + 1].stop))
    del ranges[cursor + 1]
  cursor += 1

count = sum([len(r) for r in ranges])
print(f"Part 2: {count}")

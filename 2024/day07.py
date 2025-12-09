import sys

equations = [(tmp := line.rstrip().split(": "), (int(tmp[0]), [int(x) for x in tmp[1].split(" ")]))[1] for line in sys.stdin.readlines()]

def descent(operands, concat = False) :
  if len(operands) == 1 :
    yield operands[0]
  else :
    for x in descent(operands[:-1], concat) :
      yield x + operands[-1]
      yield x * operands[-1]
      if concat :
        yield int(str(x) + str(operands[-1]))

total = 0
for result, operands in equations :
  if any([result == r for r in descent(operands)]) :
    total += result

print(f"Part 1: {total}")

total = 0
for result, operands in equations :
  if any([result == r for r in descent(operands, True)]) :
    total += result

print(f"Part 2: {total}")


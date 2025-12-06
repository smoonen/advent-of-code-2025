import sys
from functools import reduce

OPCODES = { '+' : sum, '*' : lambda x : reduce(int.__mul__, x) }

text = [line for line in sys.stdin.readlines()]

matrix = zip(*[line.split() for line in text])
result = sum([OPCODES[z[-1]]([int(x) for x in z[:-1]]) for z in matrix])

print(f"Part 1: {result}")

# For part 2, flip the character matrix of the input
# It's important not to rstrip the input above because it consumes spaces as well as newlines,
# and it was very nice of the author to include excess spaces so that we can flip the input readily!

matrix = [''.join(line) for line in zip(*text)]

# Successive operations are separated by blanks and do not have a uniform number of inputs.
# Therefore we have to collect them.
def split(inp) :
  collector = []
  for operand in inp :
    if operand.isspace() :
      yield collector
      collector = []
    else :
      collector.append(operand)
  if collector :
    yield collector

# I observe that the opcode is always attached to the "first" (last according to the instructions, but these are all associative operations) number
result = sum([OPCODES[operands[0][-1]]([int(operands[0][:-1])] + [int(x) for x in operands[1:]]) for operands in split(matrix)])

print(f"Part 2: {result}")

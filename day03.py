import functools, sys

# Convert list of bank strings into list of list of numbers
banks = list([bank.rstrip() for bank in sys.stdin.readlines()])

#       v Sum the max value for each bank
#              v For each bank, iterate through first char using range to generate index, and find the max combo
#                    v find max possible jolt for each given index in this bank
total = sum( [ max([ int(bank[x] + max(bank[x+1:])) for x in range(len(bank) - 1) ]) for bank in banks])

print(f"Part 1: {total}")

# For part 2 we have to go recursive.
# Naive approach: visit each combination and memoize.
#jolt = functools.cache(lambda substring, depth : max([ substring[x] + ("" if depth == 1 else jolt(substring[x+1:], depth - 1)) for x in range(len(substring) + 1 - depth) ]))
#total = sum([int(jolt(bank, 12)) for bank in banks])

# Better approach: shortcut suboptimal digits (thanks, Brian!)
jolt = lambda substring, depth : \
  max(substring) if depth == 1 \
    else (tmp_digit := max(substring[:-(depth-1)]),
          tmp_digit + jolt(substring[substring.index(tmp_digit)+1:], depth - 1))[1]

total = sum([int(jolt(bank, 12)) for bank in banks])

print(f"Part 2: {total}")


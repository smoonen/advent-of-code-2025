from functools import reduce
import sys

STATE = (50, 0)

# Calculate the incremental amount for a given instruction; for example, L5 yields -5
amount = lambda x : (1 if x[0] == 'R' else -1) * int(x[1:])

# Given a starting and ending number, determine how many times we passed zero.
# The zero counter has three variations:
#   - If we move right, it is simply the div of the current state plus the increment
#   - If we move left *starting at zero*, it is simply the div of the absolute value of the increment
#   - Otherwise if we move left, we need to absolutize the div from a negative rather than positive starting point
perform_increment = lambda state, instruction : \
  (tmp_increment := amount(instruction),
   ((state[0] + tmp_increment) % 100,
    state[1] + ((state[0] + tmp_increment) // 100 if tmp_increment > 0 \
                 else (100 - state[0] - tmp_increment) // 100 if state[0] > 0 \
                 else (-tmp_increment) // 100)))[-1]

# Reduce the input given our starting state
result = reduce(perform_increment, sys.stdin.readlines(), STATE)

print(result[1])

# 6806 is too high
# 6379 is too high
print(perform_increment((50, 0), "L50"))
print(perform_increment((50, 0), "R50"))
print(perform_increment((50, 0), "L5"))
print(perform_increment((50, 0), "R5"))
print(perform_increment((50, 0), "L500"))
print(perform_increment((50, 0), "R500"))
print(perform_increment((50, 0), "L550"))
print(perform_increment((50, 0), "R550"))


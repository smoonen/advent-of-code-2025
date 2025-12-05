from functools import reduce
import sys

STATE = (50, 0)
combination = sys.stdin.readlines()

# Calculate the incremental amount for a given instruction; for example, L5 yields -5
amount = lambda x : (1 if x[0] == 'R' else -1) * int(x[1:])

# Part 1: Count those times where we end up at zero.

perform_increment = lambda state, instruction : (tmp_result := (state[0] + amount(instruction)) % 100, state[1] + (tmp_result == 0))

# Reduce the input given our starting state
result = reduce(perform_increment, combination, STATE)

print(f"Method 1: {result[1]}")

# Part 2: Given a starting and ending number, determine how many times we passed zero.
# The zero counter has two variations:
#   - If we move right, it is simply the div of the current state plus the increment
#   - If we move left, absolutize the div from negative starting point = (100 - start) % 100
perform_increment = lambda state, instruction : \
  (tmp_increment := amount(instruction),
   ((state[0] + tmp_increment) % 100,
    state[1] + ((state[0] + tmp_increment) // 100 if tmp_increment > 0 else ((100 - state[0]) % 100 - tmp_increment) // 100)))[-1]

# Reduce the input given our starting state
result = reduce(perform_increment, combination, STATE)

print(f"Method 2: {result[1]}")


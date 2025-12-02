import re, sys

counter = 0
ranges = sys.stdin.readline()[:-1].split(',')

for item in ranges :
  start, end = map(int, item.split('-'))
  for sku in range(start, end + 1) :
    if re.match(r"^(\d+)\1$", str(sku)) :
      counter += sku

print(f"Part 1: {counter}")

counter = 0
for item in ranges :
  start, end = map(int, item.split('-'))
  for sku in range(start, end + 1) :
    if re.match(r"^(\d+)\1+$", str(sku)) :
      counter += sku

print(f"Part 2: {counter}")


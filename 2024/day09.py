import copy, sys

descriptor = sys.stdin.readline().rstrip()

is_file = True
cur_id = 0
blocks = []
while len(descriptor) :
  blocks.extend([cur_id if is_file else None] * int(descriptor[0]))
  if is_file :
    cur_id += 1
  is_file = not is_file
  descriptor = descriptor[1:]

p1blocks = copy.copy(blocks)
while None in p1blocks :
  if p1blocks[-1] is None :
    p1blocks = p1blocks[:-1]
  else :
    block = p1blocks[-1]
    p1blocks = p1blocks[:-1]
    p1blocks[p1blocks.index(None)] = block

checksum = sum([i * p1blocks[i] for i in range(len(p1blocks))])
print(f"Part 1: {checksum}")

cur_id -= 1
p2blocks = copy.copy(blocks)
while cur_id >= 0 : # Work backwards through files
  file_ix = p2blocks.index(cur_id)
  file_len = p2blocks.count(cur_id)

  # Find leftmost batch of None that could fit us
  # Note: the rule is that we need a full batch; shifting left to overlap ourselves is not necessary
  for ix in range(file_ix) :
    if p2blocks[ix:ix+file_len].count(None) == file_len :
      p2blocks[ix:ix+file_len] = [cur_id] * file_len
      p2blocks[file_ix:file_ix+file_len] = [None] * file_len
      break

  cur_id -= 1

checksum = sum([i * p2blocks[i] for i in range(len(p2blocks)) if p2blocks[i] is not None])
print(f"Part 2: {checksum}")


ranges = []
available = []

with open('day5_input.txt','r') as f:
  flag = False
  for line in f:
    if len(line.strip()) == 0:
      flag = True
    elif not flag:
      ranges.append([int(x) for x in line.strip().split('-')])
    else:
      available.append(int(line.strip()))

# part 1
count = 0
for ingr in available:
  fresh = False
  for rang in ranges:
    if rang[0] <= ingr <= rang[1]:
      fresh = True
  if fresh:
    count += 1

print('part1:', count)

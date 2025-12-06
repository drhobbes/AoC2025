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

# part 2
first_id = [rng[0] for rng in ranges]
secnd_id = [rng[1] for rng in ranges]
first_id = sorted(first_id)
secnd_id = sorted(secnd_id)

merged = []
index = 0
while index < len(ranges):
  first = first_id[index]
  while index < len(ranges)-1 and secnd_id[index] >= first_id[index+1]:
    index += 1
  merged.append([first, secnd_id[index]])
  print(merged[-1])
  index += 1

total = 0
for rang in merged:
  total += rang[1] - rang[0] + 1
print('part2:', total)

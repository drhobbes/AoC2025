import math

with open('day2_input.txt','r') as f:
  ranges = [(x.split('-')[0], x.split('-')[1]) for x in f.readline().split(',')]

# part 1
invalid_total = 0

for rang in ranges:
  start_prefix = rang[0][:len(rang[0])//2]
  if start_prefix == '':
    start_prefix = 0
  end_prefix = rang[1][:math.ceil(len(rang[1])/2)]
  
  start_val, end_val = int(rang[0]), int(rang[1])
  
  while int(start_prefix) <= int(end_prefix):
    if start_val <= int(start_prefix+start_prefix) <= end_val:
      invalid_total += int(start_prefix+start_prefix)
    start_prefix = str(int(start_prefix)+1)

print('part1:',invalid_total)

# part 2
def is_repeats(num):
  num = str(num)
  for pref_len in range(1,len(num)//2+1):
    prefix = num[:pref_len]
    num_pref = len(num)//pref_len
    if num == prefix*num_pref:
      return True
  return False

invalid_total = 0

for rang in ranges:
  start_val, end_val = int(rang[0]), int(rang[1])
  while start_val <= end_val:
    if is_repeats(start_val):
      print(start_val)
      invalid_total += start_val
    start_val += 1

print('part2:',invalid_total)

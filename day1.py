lines = []
with open('day1_input.txt','r') as f:
  for line in f:
    lines.append(int(line[1:-1].strip()))
    if line[0] == 'L':
      lines[-1] *= -1

index = 50
num_zeroes = 0

# part 1
for line in lines:
  index += line
  index %= 100
  if index == 0:
    num_zeroes += 1

print('password:', num_zeroes)

index = 50
num_zeroes = 0

# part 2
for line in lines:
  index += line
  num_zeroes += abs(index // 100)
  index %= 100

print('password2:', num_zeroes)

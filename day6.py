# part 1
values = []
with open('day6_input.txt','r') as f:
  for line in f:
    if line.strip()[0].isdigit():
      values.append([int(x) for x in line.strip().split()])
    else:
      operators = line.strip().split()
      
total = 0
for i in range(len(operators)):
  if operators[i] == '+':
    subtotal = 0
    for line in values:
      subtotal += line[i]
  else:
    subtotal = 1
    for line in values:
      subtotal *= line[i]
  total += subtotal

print('part1:', total)

# OKAY FINE I'LL READ THIS IN AGAIN part 2
values = []
with open('day6_input.txt', 'r') as f:
  for line in f:
    if line.strip()[0].isdigit():
      values.append(line[:-1])
    else:
      operators = line[:-1]

total = 0
problem_numbers = []
for i in list(range(len(operators)))[::-1]:
  # construct the number
  number = ''
  for line in values:
    if line[i] == ' ':
      pass
    else:
      number += line[i]
  if len(number) > 0:
    problem_numbers.append(int(number))

  # and then just do the same thing as part 1
  if operators[i] == '+':
    total += sum(problem_numbers)
    problem_numbers = []
  elif operators[i] == '*':
    subtotal = 1
    for num in problem_numbers:
      subtotal *= num
    total += subtotal
    problem_numbers = []

print('part2:',total)

banks = []
with open('day3_input.txt','r') as f:
  for line in f:
    banks.append(line.strip())

def best_digit(bank, remaining_digits):
  max_index = 0
  for i in range(len(bank)-remaining_digits):
    if bank[i] > bank[max_index]:
      max_index = i
  return max_index

# part 1
total = 0
for bank in banks:
  first = best_digit(bank,1)
  second = first + 1 + best_digit((bank[first+1:]),0)
  total += int(bank[first]+bank[second])

print('part 1:', total)

# part 2
total = 0
for bank in banks:
  num = ''
  prev_index = 0
  for remain in list(range(12))[::-1]:
    index = best_digit(bank[prev_index:], remain)
    num += bank[prev_index + index]
    prev_index += index + 1
  total += int(num)

print('part 2:', total)

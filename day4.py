layout = []
with open('day4_input.txt','r') as f:
  for line in f:
    layout.append([ch for ch in line.strip()])

def safe_roll_check(row, col):
  if 0 <= row < len(layout) and 0 <= col < len(layout[row]):
    return layout[row][col] == '@'

def is_accessible(row, col):
  num_rolls = 0
  for i in (row-1, row, row+1):
    for j in (col-1, col, col+1):
      if (i,j) != (row, col):
        num_rolls += 1 if safe_roll_check(i,j) else 0
  return num_rolls < 4

# part 1
total = 0
for row in range(len(layout)):
  for col in range(len(layout[row])):
    if layout[row][col] == '@':
      total += 1 if is_accessible(row, col) else 0

print('part 1:', total)

# part 2
def copy_layout():
  new_layout = []
  for line in layout:
    new_layout.append(line[:])
  return new_layout

total = 0
done = False
while not done:
  new_layout = copy_layout()
  subtotal = 0
  for row in range(len(layout)):
    for col in range(len(layout[row])):
      if layout[row][col] == '@':
        if is_accessible(row,col):
          subtotal += 1
          new_layout[row][col] = '.'
  if subtotal > 0:
    total += subtotal
    layout = new_layout
  else:
    done = True

print('part 2:', total)

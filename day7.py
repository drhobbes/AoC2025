layout = []
with open('day7_input.txt','r') as f:
  for line in f:
    layout.append([ch for ch in line.strip()])

# part 1
beam_index = layout[0].index('S')

def trace_beams(beam_index, row):
  if row == len(layout):
    return

  if layout[row][beam_index] == '^':
    if layout[row][beam_index-1] != '|':
      layout[row][beam_index-1] = '|'
      trace_beams(beam_index-1, row+1)
    if layout[row][beam_index+1] != '|':
      layout[row][beam_index+1] = '|'
      trace_beams(beam_index+1, row+1)
  else:
    layout[row][beam_index] = '|'
    trace_beams(beam_index, row+1)

trace_beams(beam_index, 1)
total = 0
for line_index in range(1, len(layout)):
  for index in range(len(layout[line_index])):
    if layout[line_index][index] == '^' and layout[line_index-1][index] == '|':
      total += 1
print('part1:',total)

# part 2
beam_index = layout[0].index('S')
layout[0][beam_index] = 1

for row in range(1, len(layout)):
  for i in range(len(layout[row])):
    if isinstance(layout[row-1][i], int):
      if layout[row][i] == '^':
        if isinstance(layout[row][i-1], int):
          layout[row][i-1] += layout[row-1][i]
        else:
          layout[row][i-1] = layout[row-1][i]
        layout[row][i+1] = layout[row-1][i]
      else:
        if isinstance(layout[row][i], int):
          layout[row][i] += layout[row-1][i]
        else:
          layout[row][i] = layout[row-1][i]

print('part2:',sum([x for x in layout[-1] if isinstance(x, int)]))

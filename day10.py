lights = []
buttons = []
joltage = []
states = []

with open('day10_babyinput.txt','r') as f:
  for line in f:
    parts = line.strip().split()
    schematic = []
    for part in parts:
      if part[0] == '[':
        lights.append(part[1:-1])
      elif part[0] == '(':
        schematic.append([int(x) for x in part[1:-1].split(',')])
      else:
        joltage.append([int(x) for x in part[1:-1].split(',')])
    buttons.append(schematic)
    states.append(dict())

def press(button, state):
  result = ''
  for i in range(len(state)):
    if i in button:
      result += '.' if state[i] == '#' else '#'
    else:
      result += state[i]
  return result

def push_buttons(index, current_state):
  if current_state == lights[index]:
    return

  updated = []
  for button in buttons[index]:
    new_state = press(button, current_state)
    if new_state not in states[index]:
      states[index][new_state] = states[index][current_state]+1
      updated.append(new_state)
    elif states[index][new_state] > states[index][current_state]+1:
      states[index][new_state] = states[index][current_state]+1
      updated.append(new_state)

  # not much of an optimization but it's something
  if lights[index] in updated:
    return
  
  for state in updated:
    push_buttons(index, state)
  
# part 1
#total = 0
#for i in range(len(lights)):
#  start = '.'*len(lights[i])
#  states[i][start] = 0
#  push_buttons(i, start)
#  total += states[i][lights[i]]
#print('part1:',total)

# part 2
def jolt_press(button, state):
  result = state[:]
  for i in button:
    result[i] += 1
  return result

total = 0
for i in range(len(joltage)):
  # record the initial index of each joltage
  goal_state = {joltage[i][j]:j for j in range(len(joltage[i]))}

  # split out the buttons that could contribute to each joltage
  button_group = []
  for j in range(len(joltage[i])):
    button_group.append(list())
    for button in buttons[i]:
      if j in button:
        button_group[j].append(button)

  # if any group only has one value in it, press that button that number of times
  state = [0]*len(joltage[i])
  subtotal = 0
  for j in range(len(button_group)):
    if len(button_group[j]) == 1:
      for k in range(joltage[i][j]):
        state = jolt_press(button_group[j][0], state)
      subtotal += joltage[i][j]
      # and remove that button as an option from everywhere else
      for group in button_group:
        if button_group[j][0] in group:
          del group[group.index(button_group[j][0])]

  

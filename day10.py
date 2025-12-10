lights = []
buttons = []
joltage = []
states = []
jolt_states = []

with open('day10_input.txt','r') as f:
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
    jolt_states.append(dict())

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
total = 0
for i in range(len(lights)):
  start = '.'*len(lights[i])
  states[i][start] = 0
  push_buttons(i, start)
  total += states[i][lights[i]]
print('part1:',total)

def puth_more_buttons(index, current_state):
  for i in range(len(current_state)):
    if current_state[i] > joltage[index][i]:
      return False

  updated = []

shapes = []
dimensions = []
requirements = []

with open('day12_babyinput.txt','r') as f:
  shape_mode = True
  shape = []
  for line in f:
    line = line.strip()
    if len(line) == 0:
      shapes.append(shape)
    elif not shape_mode or 'x' in line:
      shape_mode = False
      dim = line.split(':')
      dimensions.append([int(dim[0].split('x')[0]), int(dim[0].split('x')[1])])
      requirements.append([int(x) for x in dim[1].split()])
    else:
      if ':' in line:
        shape = []
      else:
        shape.append(line)

count = 0
for region in range(len(dimensions)):
  pass

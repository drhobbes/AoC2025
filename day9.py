red_tiles = []
with open('day9_input.txt','r') as f:
  for line in f:
    red_tiles.append([int(x) for x in line.strip().split(',')])

max_area = 0
for i in range(len(red_tiles)-1):
  for j in range(i+1, len(red_tiles)):
    xdist = abs(red_tiles[i][0]-red_tiles[j][0]+1)
    ydist = abs(red_tiles[i][1]-red_tiles[j][1]+1)
    area = xdist*ydist
    if area > max_area:
      max_area = area

print('part1:', max_area)


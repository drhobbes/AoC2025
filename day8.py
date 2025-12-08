import math

how_many = 1000

points = []
with open('day8_input.txt','r') as f:
  for line in f:
    points.append([int(x) for x in line.strip().split(',')])

def distance(x, y):
  return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)

distances = []
for i in range(len(points)):
  for j in range(i+1,len(points)):
    distances.append([distance(points[i],points[j]), i, j])
distances = sorted(distances, key=lambda x: x[0])

circuits = [[x] for x in range(len(points))]

def find_circ(point_index):
  for circ in range(len(circuits)):
    if point_index in circuits[circ]:
      return circ

# part 1
for dist in distances[:how_many]:
  c1 = find_circ(dist[1])
  c2 = find_circ(dist[2])

  if c1 == c2:
    pass
  else:
    circuit1 = circuits[c1]
    circuit2 = circuits[c2]
    del circuits[max(c1,c2)]
    del circuits[min(c1,c2)]

    circuits.append(circuit1+circuit2)

circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
print("part1:", len(circuits[0])*len(circuits[1])*len(circuits[2]))

# part 2
i = how_many
while len(circuits) > 1:
  dist = distances[i]
  i += 1
  c1 = find_circ(dist[1])
  c2 = find_circ(dist[2])

  if c1 == c2:
    pass
  else:
    circuit1 = circuits[c1]
    circuit2 = circuits[c2]
    del circuits[max(c1,c2)]
    del circuits[min(c1,c2)]

    circuits.append(circuit1+circuit2)

x1 = points[distances[i-1][1]][0]
x2 = points[distances[i-1][2]][0]
print("part2:",x1*x2)

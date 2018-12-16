file = open("input.txt", "r")
lines = file.readlines()
patch = list()
count = 0
for line in lines:
    line = line.strip()

for i in range(1000):
    for j in range(1000):
        if j == 0:
            patch.append(list())
        patch[i].append(0)

for line in lines:
    items = line.split(" ")
    coords = items[2][:-1].split(",")
    dimensions = items[3].split("x")
    width = range(int(dimensions[0]))
    height = range(int(dimensions[1]))
    for x in width:
        for y in height:
            patch[y + int(coords[1])][x + int(coords[0])] += 1
            if patch[y + int(coords[1])][x + int(coords[0])] == 2:
                count += 1
print(count)

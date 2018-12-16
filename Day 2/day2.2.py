file = open("day2-input.txt", "r")
data = file.readlines()
length = range(len(data))

for i in length:
    data[i] = data[i].strip()
    for line in data:
        count = 0
        line = line.strip()
        for x in range(len(line)):
            if line[x] != data[i][x]:
                count += 1
        if count == 1:
            print(line)

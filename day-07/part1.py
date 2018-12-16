file = open("input.txt", "r")
lines = file.readlines()

tasks = {}
completedTasks = list()
numTasks = 0

for line in lines:
    line = line.strip()
    before = line[5]
    task = line[-12]

    if task not in tasks:
        tasks[task] = list()
        numTasks += 1
    if before not in tasks:
        tasks[before] = list()
        numTasks += 1

    tasks[task].append(before)

out = ""

while numTasks > 0:
    availableTasks = list()
    for x in tasks:
        possible = True
        for required in tasks[x]:
            if required not in completedTasks:
                possible = False
        if possible and x not in list(out):
            availableTasks.append(x)

    availableTasks.sort()

    out += availableTasks[0]

    completedTasks.append(availableTasks[0])

    numTasks -= 1

print(out)

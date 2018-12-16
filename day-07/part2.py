file = open("input.txt", "r")
lines = file.readlines()

tasks = {}
completedTasks = list()
workingTasks = list()
numTasks = 0
workers = [{"time": 0, "item": ""}, {"time": 0, "item": ""}, {"time": 0, "item": ""}, {"time": 0, "item": ""}, {"time": 0, "item": ""}]
timeElapsed = 0

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

def convertToTime(x):
    return 61 + ord(x) - ord("A")

while numTasks > 0:
    availableTasks = list()
    for x in tasks:
        possible = True
        for required in tasks[x]:
            if required not in completedTasks:
                possible = False
        if possible and x not in completedTasks and x not in workingTasks:
            availableTasks.append(x)
    numbWorkers = 0
    for x in workers:
        if x["time"] == 0:
            numbWorkers += 1
    availableTasks.sort()
    if len(availableTasks) == 0 or numbWorkers == 0:
        minLength = 999
        for i in workers:
            if i["time"] < minLength and i["time"] != 0:
                minLength = i["time"]
        for i in range(len(workers)):
            if workers[i]["time"] != 0:
                workers[i]["time"] -= minLength
                if workers[i]["time"] == 0:
                    workingTasks.remove(workers[i]["item"])
                    completedTasks.append(workers[i]["item"])
                    numTasks -= 1
        timeElapsed += minLength
    else:
        for i in range(len(workers)):
            if workers[i]["time"] == 0:
                workers[i]["time"] = convertToTime(availableTasks[0])
                workers[i]["item"] = availableTasks[0]
                workingTasks.append(availableTasks[0])
                break

print(timeElapsed)

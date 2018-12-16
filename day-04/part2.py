import datetime

file = open("input.txt", "r")
lines = file.readlines()

guards = {}
days = {}
max = 0
maxGuard = 0
maxMinute = 0

def getTimeObj(items):
    dateTime = items.split(" ")
    dateObj = datetime.datetime.strptime(dateTime[0], "%Y-%m-%d").date()
    if dateTime[1][0] != "0":
        dateObj += datetime.timedelta(days=1)
    return dateObj.strftime('%Y%m%d')

for line in lines:
    line = line.strip()
    items = line.replace("[", "").split("]")
    if line[-1:] == "t":
        guard = int(items[1].split("#")[1].split(" ")[0])
        dateObj = getTimeObj(items[0])
        guards[dateObj] = guard

for line in lines:
    line = line.strip()
    items = line.replace("[", "").split("]")
    if line[-1:] == "p":
        dateObj = getTimeObj(items[0])
        guard = guards[dateObj]
        if guard not in days:
            days[guard] = {"wake": list(), "sleep": list(), "times": {}}
        if line[-2:] == "up":
            days[guard]["wake"].append(dateObj + items[0].split(":")[1])
        elif line[-2:] == "ep":
            days[guard]["sleep"].append(dateObj + items[0].split(":")[1])

for guard in days:
    days[guard]["wake"].sort()
    days[guard]["sleep"].sort()
    for w in days[guard]["sleep"]:
        dateW = w[:8]
        timeW = int(w[-2:])
        for s in days[guard]["wake"]:
            dateS = s[:8]
            timeS = int(s[-2:])
            if dateS == dateW and timeW < timeS:
                for i in range(timeW, timeS):
                    try:
                        days[guard]["times"][i] += 1
                    except:
                        days[guard]["times"][i] = 1
                    if days[guard]["times"][i] > max:
                        max = days[guard]["times"][i]
                        maxMinute = i
                        maxGuard = guard
                break

print(maxMinute * maxGuard)

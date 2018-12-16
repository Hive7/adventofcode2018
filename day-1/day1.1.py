file = open("day1-input.txt", "r")
lines = file.readlines()
start = 0

for x in lines:
    x = x.replace("\n", "")
    start = start + int(x)

print(start)
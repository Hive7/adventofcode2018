file = open("input.txt", "r")
lines = file.readlines()
start = 0
array = list()
array.append(start)
found = True
while found:
    for x in lines:
        x = x.replace("\n", "")
        start = start + int(x)
        if start in array:
            found = False
            break
        array.append(start)
    print(start)
print(start)

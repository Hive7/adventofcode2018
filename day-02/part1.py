file = open("input.txt", "r")
data = file.readlines()

two = 0
three = 0

for line in data:
    stripped = line.strip()
    th = True
    tw = True
    for x in stripped:
        count = 0
        for i in stripped:
            if x == i:
                count += 1
        if count == 2 and tw:
            two += 1
            tw = False
        elif count == 3 and th:
            three += 1

print(str(two * three))

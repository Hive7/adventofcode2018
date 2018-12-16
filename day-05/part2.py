file = open("input.txt", "r")
string = file.readline().strip()

def flipCase(char):
    if char.upper() == char:
        return char.lower()
    else:
        return char.upper()

min = 99999

chars = list()

for x in string:
    if x.lower() not in chars:
        chars.append(x.lower())

for x in chars:
    temp = string.replace(x, "").replace(x.upper(), "")
    i = 0
    while True:
        if flipCase(temp[i]) == temp[i + 1]:
            temp = temp[:i] + temp[(i + 2):]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
        if i >= len(temp) - 1:
            break
    if len(temp) < min:
        min = len(temp)

print(min)

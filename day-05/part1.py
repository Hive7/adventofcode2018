file = open("input.txt", "r")
string = file.readline().strip()

def flipCase(char):
    if char.upper() == char:
        return char.lower()
    else:
        return char.upper()

i = 0
while True:
    if flipCase(string[i]) == string[i + 1]:
        string = string[:i] + string[(i + 2):]
        i -= 1
        if i < 0:
            i = 0
    else:
        i += 1
    if i >= len(string) - 1:
        break

print(len(string))

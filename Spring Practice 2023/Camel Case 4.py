import sys

def splitName(line):
    temp = ""
    for i in line:
        if i.isupper(): temp += " " + i.lower(); continue
        temp += i
    if method == "M": temp = temp[:-2]
    elif method == "C": temp = temp.lstrip()
    return temp
            
def combineName(line):
    temp = ""
    for ind, i in enumerate(line):
        if i.islower() and line[ind-1] == " ":
            temp += i.upper()
            continue
        temp += i
    temp = temp.replace(" ", "")
    if method == "M": temp += "()"
    elif method == "C": temp = temp[0].upper() + temp[1:]
    return temp

lines = ""
for line in sys.stdin.read().split("\r\n"):
    operation, method, name = line.split(";")
    if operation == "S":
        line = splitName(name)
    else:
        line = combineName(name)
    lines += line+"\r\n"
print(lines[:-2])
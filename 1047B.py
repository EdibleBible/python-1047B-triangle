f = open("1047B.txt", "r")
f.readline()
max = 0
for string in f:
    localmax = int(string.split(" ")[0]) + int(string.split(" ")[1])
    if max < localmax:
        max = localmax
print(max)
f.close()
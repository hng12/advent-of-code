f = open("input.txt", "r")
arr = []
arr.append(f.readline()[0:-1])
for x in f:
    if x == '\n':
        arr.append(f.readline()[0:-1])
    else:
        arr[-1] = int(arr[-1]) + int(x[0:-1])
maxs = []
for i in range(3):
    max = [0,0]
    for i in range(len(arr)):
        if int(arr[i]) > max[0]:
            max[0] = int(arr[i])
            max[1] = i
    maxs.append(max[0])
    arr.pop(max[1])

print(sum(maxs))
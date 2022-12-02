f = open("input.txt", "r")
lines = f.readlines()
lines = list(map(int, lines))
previous = 100000000
count = 0
for i in range(len(lines)-2):
    window = lines[i] + lines[i+1] + lines[i+2]
    if window > previous:
        count += 1
    previous = window
print(count)

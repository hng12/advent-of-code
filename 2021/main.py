import re
f = open("input.txt", "r")
lines = f.readlines()
horizontal = 0
vertical = 0
aim = 0
for line in lines:
    if line.find('forward') == 0:
        horizontal += int(re.search('[0-9]', line).group())
        vertical += int(re.search('[0-9]', line).group())*aim
    elif line.find('up') == 0:
        aim -= int(re.search('[0-9]', line).group())
    elif line.find('down') == 0:
        aim += int(re.search('[0-9]', line).group())

print(horizontal*vertical)
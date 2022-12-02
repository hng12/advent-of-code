f = open("input.txt", "r")
lines = f.readlines()
moves = {
    'A': {
      'Z': 2,
      'X': 3,
      'Y': 1,
    },
    'B': {
      'Z': 3,
      'X': 1,
      'Y': 2,
    },
    'C': {
      'Z': 1,
      'X': 2,
      'Y': 3,
    }
}
points = 0
for line in lines:
    plays = line.split()
    if plays[1] == 'X':
        points += moves[plays[0]]['X']
    elif plays[1] == 'Y':
        points += 3
        points += moves[plays[0]]['Y']
    elif plays[1] == 'Z':
        points += 6
        points += moves[plays[0]]['Z']

print(points) 

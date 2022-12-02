f = open("input.txt", "r")
lines = f.readlines()
moves = {
    'X': {
      'win' : 'C',
      'lose': 'B',
      'draw': 'A',
      'score': 1
    },
    'Y': {
      'win': 'A',
      'lose': 'C',
      'draw': 'B',
      'score': 2
    },
    'Z': {
      'win': 'B',
      'lose': 'A',
      'draw': 'C',
      'score': 3
    }
}
points = 0
for line in lines:
    plays = line.split()
    if plays[0] == moves[plays[1]]['win']:
        points += 6
    elif plays[0] == moves[plays[1]]['draw']:
        points += 3
    points += moves[plays[1]]['score']

print(points) 

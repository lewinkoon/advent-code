from collections import defaultdict

with open('input.txt', 'r') as file:
    matrix = defaultdict(str) | {(i, j): c for i, row in enumerate(file) for j, c in enumerate(row)}

    keys = list(matrix.keys())
    directions = -1,0,1

    target = list('MAS'), list('SAM')
    total = sum([matrix[i+d, j+d] for d in directions] in target
          and [matrix[i+d, j-d] for d in directions] in target for i,j in keys)

    print(total)

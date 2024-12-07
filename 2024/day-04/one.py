from collections import defaultdict

with open('input.txt', 'r') as file:
    matrix = defaultdict(str) | {(i, j): c for i, row in enumerate(file) for j, c in enumerate(row)}

    keys = list(matrix.keys())
    directions = -1,0,1

    target = list('XMAS'),
    total = sum([matrix[i+di*n, j+dj*n] for n in range(4)] in target for di in directions for dj in directions for i,j in keys)

    print(total)

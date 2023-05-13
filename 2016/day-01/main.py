import numpy as np

def p1():
    with open("input.txt", "r") as file:
        data = file.read().rstrip().split(", ")

    position = 0 + 0j
    direction = 0 + 1j

    for step in data:
        if step[0] == 'L':
            direction *= 1j
        else:
            direction *= -1j

        length = int(step[1:])

        for _ in range(0, length):
            position += direction
            
    res = int(abs(position.real) + abs(position.imag))
    print("Part one:", res)

def p2():
    with open("input.txt", "r") as file:
        data = file.read().rstrip().split(", ")

    position = 0 + 0j
    direction = 0 + 1j
    grid = np.ndarray((2000,2000))

    grid[0,0] = 1
    res = None

    for step in data:
        if step[0] == 'L':
            direction *= 1j
        else:
            direction *= -1j

        length = int(step[1:])

        for _ in range(0, length):
            position += direction

            grid[int(position.real)][int(position.imag)] += 1
            if grid[int(position.real)][int(position.imag)] >= 2 and res == None:
                res = int(abs(position.real) + abs(position.imag))
            
    print("Part two:", res)

if __name__ == "__main__":
    p1()
    p2()

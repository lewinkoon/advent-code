file_path = "input.txt"

def check(list):
    inc = [list[i + 1] - list[i] for i in range(len(list) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
            return True
    return False


reports = 0
with open(file_path, 'r') as file:
    for line in file:
        levels = [int(x) for x in line.split()]
        if check(levels):
            reports += 1
    print(reports)

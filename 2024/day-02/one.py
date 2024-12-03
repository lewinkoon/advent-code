file_path = "input.txt"

def sign(x):
    if x > 0:
        return False
    elif x < 0:
       return True
    else:
       return None


with open(file_path, 'r') as file:
    reports = 0
    for line in file:
        levels = [int(x) for x in line.split()]
        gradient = sign(levels[0] - levels[len(levels)-1])
        condition = [False] * (len(levels) - 1)
        for i in range(len(levels) - 1):
            diff = levels[i]-levels[i+1]
            if 1 <= abs(diff) <= 3 and sign(diff) == gradient:
                condition[i] = True
        if all(condition):
            reports += 1
    print(reports)

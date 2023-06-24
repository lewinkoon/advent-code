def p1():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    counter = 0

    for line in data:
        line = line.strip().split()
        vals = sorted([int(x) for x in line])
        if vals[0] + vals[1] > vals[2]:
            counter += 1

    print("Part one:", counter)


def p2():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    # print("Part two:", code)


if __name__ == "__main__":
    p1()
    p2()

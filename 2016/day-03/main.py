def p1():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    n = 0

    for line in data:
        line = line.strip().split()
        vals = sorted([int(x) for x in line])
        if vals[0] + vals[1] > vals[2]:
            n += 1

    print("Part one:", n)


def p2():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    n = 0
    ll = list()
    la = list()

    for line in data:
        ll.append(list(map(int, line.lstrip().split())))

    for i in range(len(ll) // 3):
        for j in range(3):
            ln = [ll[i * 3][j], ll[i * 3 + 1][j], ll[i * 3 + 2][j]]
            ln.sort()
            la.append(ln)

    for l in la:
        if l[0] + l[1] > l[2]:
            n += 1

    print("Part two:", n)


if __name__ == "__main__":
    p1()
    p2()

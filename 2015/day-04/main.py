from hashlib import md5


def p1():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()

    for i in range(10000000):
        h = md5((data + str(i)).encode()).hexdigest()
        if h[:5] == '00000':
            output = i
            break

    print("Part one:", output)


def p2():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()

    for i in range(10000000):
        h = md5((data + str(i)).encode()).hexdigest()
        if h[:6] == '000000':
            output = i
            break

    print("Part two:", output)


if __name__ == "__main__":
    p1()
    p2()

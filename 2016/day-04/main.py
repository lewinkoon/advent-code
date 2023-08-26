from collections import Counter
import re


def mostFrequent(lst, n):
    counter = Counter(lst)
    common = counter.most_common()
    items = sorted(common, key=lambda x: (-x[1], x[0]))
    return "".join([item for item, _ in items[:5]])


def p1():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    output = 0

    for line in data:
        room = line.split("-")
        name = "".join(room[:-1])

        checksum = re.search(r"\[([a-zA-Z]+)\]", room[-1]).group(1)
        id = re.search(r"\d{3}", room[-1]).group()
        res = mostFrequent(name, 5)

        if res == checksum:
            output += int(id)

    print("Part one:", output)


def p2():
    with open("input.txt", "r") as file:
        data = file.readlines()

    output = 0

    for line in data:
        room = line.split("-")
        encrypted = "-".join(room[:-1])
        id = re.search(r"\d{3}", room[-1]).group()

        msg = ""
        for char in encrypted:
            if char.isalpha():
                msg += chr((ord(char) - ord("a") + int(id)) % 26 + ord("a"))
            else:
                msg += " "

        if "northpole" in msg:
            output = id
            break

    print("Part two:", output)


if __name__ == "__main__":
    p1()
    p2()

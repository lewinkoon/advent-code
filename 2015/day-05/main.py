import re


def countVowels(str):
    vowels = "aeiou"
    res = sum(str.count(vowel) for vowel in vowels)
    return res > 2


def countDuplicates(str):
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            return True

    return False


def checkSubtrings(str):
    substrings = ["ab", "cd", "pq", "xy"]
    for substr in substrings:
        if substr in str:
            return False

    return True


def repeatingPairs(str):
    pattern = r"(\w\w)(?=.*\1)"
    return bool(re.search(pattern, str))


def letterBetween(str):
    pattern = r"(\w)(\w)\1"
    return bool(re.search(pattern, str))


def p1():
    with open("input.txt", "r") as file:
        data = file.readlines()

    output = 0

    for string in data:
        a = countVowels(string)
        b = countDuplicates(string)
        c = checkSubtrings(string)

        if a and b and c:
            output += 1

    print("Part one:", output)


def p2():
    with open("input.txt", "r") as file:
        data = file.readlines()

    output = 0

    for string in data:
        a = repeatingPairs(string)
        b = letterBetween(string)

        if a and b:
            output += 1

    print("Part two:", output)


if __name__ == "__main__":
    p1()
    p2()

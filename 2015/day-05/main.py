def countVowels(str):
    vowels = "aeiou"
    res = sum(str.count(vowel) for vowel in vowels)
    return res > 2


def countDuplicates(str):
    for i in range(len(str) - 1):
        if str[i] == str[i+1]:
            return True
    
    return False


def checkSubtrings(str):
    substrings = ["ab", "cd", "pq", "xy"]
    for substr in substrings:
        if substr in str:
            return False

    return True


def p1():
    with open("input.txt", "r") as file:
        data = file.readlines()

    output = 0

    for string in data:
        print(string)
        a = countVowels(string)
        b = countDuplicates(string)
        c = checkSubtrings(string)

        print(a, b, c)
        if a and b and c:
            output += 1

    print("Part one:", output)


def p2():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()

    # print("Part two:", output)


if __name__ == "__main__":
    p1()
    # p2()

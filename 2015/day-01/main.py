def main():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()

    floor = 0
    position = 0
    flag = False
    
    for i, character in enumerate(data):
        if character == "(":
            floor += 1
        elif character == ")":
            floor -= 1
        else:
            print("File is corrupted.")
            break

        if floor == -1 and flag is False:
            flag = True
            position = i
    
    print("Part one:", floor)
    print("Part two:", position)

if __name__ == "__main__":
    main()

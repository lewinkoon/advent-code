def p1():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()
        pos = [0,0]
        pos_list = ["0,0"]
        for x in data:
            if x == ">":
                    pos[0] += 1
            if x == "<":
                    pos[0] -= 1
            if x == "^":
                    pos[1] += 1
            if x == "v":
                    pos[1] -= 1
            pos_list.append(str(pos[0])+","+str(pos[1]))

    houses = len(set(pos_list))

    print("Part one:", houses)

def p2():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()
        santa_pos = [0,0]
        robo_pos = [0,0]
        pos_list = ["0,0"]

        i = 0
        for x in data:
            i += 1
            if i % 2 == 0:
                if x == ">":
                        santa_pos[0] += 1
                if x == "<":
                        santa_pos[0] -= 1
                if x == "^":
                        santa_pos[1] += 1
                if x == "v":
                        santa_pos[1] -= 1
                pos_list.append(str(santa_pos[0])+","+str(santa_pos[1]))
            else:
                if x == ">":
                        robo_pos[0] +=1
                if x == "<":
                        robo_pos[0] -=1
                if x == "^":
                        robo_pos[1] +=1
                if x == "v":
                        robo_pos[1] -=1
                pos_list.append(str(robo_pos[0])+","+str(robo_pos[1]))


    houses = len(set(pos_list))

    print("Part two:", houses)

if __name__ == "__main__":
    p1()
    p2()

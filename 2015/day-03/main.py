def p1():
    with open("input.txt", "r") as file:
        data = file.read().rstrip()
        coords = [0,0]
        coords_list = ["0,0"]
        for x in data:
            match x:
                case ">":
                    coords[0] += 1
                case "<":
                    coords[0] -= 1
                case "^":
                    coords[1] += 1
                case "v":
                    coords[1] -= 1
            coords_list.append(str(coords[0])+","+str(coords[1]))

    houses = len(set(coords_list))

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
                match x:
                    case ">":
                            santa_pos[0] += 1
                    case "<":
                            santa_pos[0] -= 1
                    case "^":
                            santa_pos[1] += 1
                    case "v":
                            santa_pos[1] -= 1
                pos_list.append(str(santa_pos[0])+","+str(santa_pos[1]))
            else:
                match x:
                    case ">":
                            robo_pos[0] +=1
                    case "<":
                            robo_pos[0] -=1
                    case "^":
                            robo_pos[1] +=1
                    case "v":
                            robo_pos[1] -=1
                pos_list.append(str(robo_pos[0])+","+str(robo_pos[1]))


    houses = len(set(pos_list))

    print("Part two:", houses)

if __name__ == "__main__":
    p1()
    p2()

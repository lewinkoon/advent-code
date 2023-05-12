def p1():
    surface = 0
    for line in open("input.txt"):
        l, w, h = [int(i) for i in line.split("x")]
        area = 2*l*w+2*w*h+2*h*l
        slack = min(l*w, w*h, h*l)
        surface += area + slack

    print("Part one:", surface)

def p2():
    length = 0
    for line in open("input.txt"):
        l, w, h = [int(i) for i in line.split("x")]
        perimeter = min(2*l+2*w, 2*w+2*h, 2*h+2*l)
        volumen = l*w*h
        length += perimeter + volumen

    print("Part two:", length)

if __name__ == "__main__":
    p1()
    p2()

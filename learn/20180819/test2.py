for i in range(1, 10):
    for j in range(1, 10):
        if i <= j:
            print("{}*{}={:<4}".format(i, j, i*j), end="")
        else:
            print("{} {} {:<4}".format(" ", " ", " "), end="")

    print()

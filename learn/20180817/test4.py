# print a square

while True:
    width = input("width of square: ")
    width = int(width)

    print("*" * width)
    if width > 1:
        if width > 2:
            for i in range(width - 2):
                print("*", end="")
                print(" "*(width-2), end="")
                print("*")
        print("*" * width)

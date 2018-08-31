while True:
    width = int(input("input the width(odd number): "))
    if width <= 0:
        print("please input the right width!")
        continue
    if width & 1 == 0:
        print("the width should be odd number!")
        continue
    for i in range(width//2):
        vacuum = (width - 2 * i) // 2
        startNum = i*2 + 1
        print(" " * vacuum, end="")
        print("*"*startNum, end="")
        print(" "*vacuum)
    print("*"*width)
    for i in range(width//2):
        vacuum = i+1
        startNum = width - 2*vacuum
        print(" "*vacuum, end="")
        print("*"*startNum, end="")
        print(" "*vacuum)


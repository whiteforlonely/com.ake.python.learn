while True:
    num = input("input the odd number: ")
    num = int(num)
    if num % 2 == 0:
        num += 1
        print("the number should be odd, now it change to ", num)
    center = num // 2
    for i in range(-center, center+1):
        if i == 0:
            print("*" * num)
            continue
        if i < 0:
            vacuum = -i
        else:
            vacuum = i
        startNum = num - 2 * vacuum
        print(" " * vacuum + "*" * (startNum // 2 + 1)) if i < 0 else print(" " * center + "*" * (startNum // 2 + 1))

while True:
    num = input("input the odd number: ")
    num = int(num)
    if num % 2 == 0:
        num += 1
        print("the number should be odd, now it change to ", num)
    center = num // 2
    for i in range(-center, center+1):
        if i < 0:
            vacuum = center + i
        else:
            vacuum = center - i
        startNum = num - 2 * vacuum
        print(" " * vacuum + "*" * startNum + " " * vacuum)

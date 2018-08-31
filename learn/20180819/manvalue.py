
num = input("input the number or Enter to exit")
maxValue = int(num)
while num:
    temp = int(num)
    if maxValue < temp:
        maxValue = temp
    print("maxValue:", maxValue)
    num = input("input the number or Enter to exit")

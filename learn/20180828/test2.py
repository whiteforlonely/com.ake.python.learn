lst = []
for i in range(5):
    while True:
        inputNum = input("input a number: ").strip().lstrip('0')
        if inputNum.isdigit():
            lst.append(int(inputNum))
            print("the digit num of {} is: {}".format(inputNum, len(inputNum)))
            break
        else:
            print("bad Number!")

lst.sort()
print("the sort numbers: {}".format(lst))

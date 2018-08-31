# Pascal's Triangle
list0 = [1]
list1 = [1, 1]


while True:
    n = input("input a num: ")
    n = int(n)
    if n == 0:
        break
    elif n == 1:
        print(list0)
    elif n == 2:
        print(list1)
    else:
        orgList = list()
        orgList.append(list0)
        orgList.append(list1)
        for i in range(2, n):
            lst = list([1])
            tempLen = len(orgList)
            lastList = orgList[tempLen - 1]
            for j in range(len(lastList) -1):
                lst.append(lastList[j] + lastList[j+1])
            else:
                lst.append(1)
            orgList.append(lst)
            print(lst)

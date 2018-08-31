a = input("input a num: ")
" the width you input is {}".format(len(a))

b = []
if not a.isdigit():
    print("please input a number:")
else:
    lst = list(a)
    lst.reverse()
    for c in lst:
        if c not in b:
            print("the char {} count in {} is {}".format(c, a, a.count(c)))
            b.append(c)


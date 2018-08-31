

def min_max(*args):
    if not args:
        print("there is not number to calculate")
        return
    min_num = args[0]
    max_num = args[0]
    length = len(args)
    for i in range(1, length):
        if args[i] > max_num:
            max_num = args[i]
        if args[i] < min_num:
            min_num = args[i]

    return tuple(min_num, max_num)


def draw_num_triangle(n=1, reverse=False):
    if not n:
        print("the number should be more than 0")
        return

    width = len(str(n)) * 3 * n
    lst = list(range(1, n+1))
    if reverse:
        lst.reverse()

    for i in lst:
        str1 = ""
        for j in range(i, 0, -1):
            if j > 9:
                str1 += "{: >4}".format(j)
            else:
                str1 += "{: >3}".format(j)
        else:
            print("{0: >{1}}".format(str1, width))


draw_num_triangle(4)
draw_num_triangle(12)
draw_num_triangle(12, True)


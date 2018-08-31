

# Direct insertion sort
def direct_insert(lst):
    if not lst:
        return
    if len(lst) < 2:
        return
    for i in range(1, len(lst)):
        temp = lst[i]
        input_position = i
        if lst[i] >= lst[i - 1]:
            continue
        for j in range(i-1, -1, -1):
            if lst[j] > temp:
                lst[j + 1] = lst[j]
                input_position -= 1
        else:
            lst[input_position] = temp


lst = [4, 3, 4, 6, 1, 8]
direct_insert(lst)
print(lst)

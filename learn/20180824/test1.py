import datetime
# 质数的计算，通过列表
t1 = datetime.datetime.now()
lst1 = [2]
for i in range(3, 100000, 2):
    for j in lst1:
        if i % j == 0:
            break
        if j > i ** 0.5:
            lst1.append(i)
            break
    else:
        lst1.append(i)
t2 = datetime.datetime.now()
t3 = t2 - t1
print(t3.total_seconds())
print(lst1)


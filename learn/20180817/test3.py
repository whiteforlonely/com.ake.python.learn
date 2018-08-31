a = input("input a number:")
b = int(a)
digit = len(a)
for i in range(digit):
    print(b % 10, ',')
    b //= 10

b = int(a)
for i in range(digit, 0, -1):
    c = b // 10 ** (i-1)
    print(c)
    b = b-(c * 10 ** (i-1))

a = input("a: ")
b = input("b: ")
c = max(a, b)
print("c: ", c)


d = input("one number: ")
e = int(d)
f = 1
if 0 < e < 10:
    f = 1
elif e < 100:
    f = 2
elif e < 1000:
    f = 3
elif e < 10000:
    f = 4
elif e < 100000:
    f = 5
else:
    print("bigger than 5")

print("the digit is: ", f)

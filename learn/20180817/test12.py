import math

maxNum = 100000
print("2", end=" ")
count = 0
for prime in range(3, maxNum, 2):
    isPrime = True
    for i in range(2, int(math.sqrt(prime))+1):
        if prime % i == 0:
            isPrime = False
            break
    if isPrime:
        print(prime, end=" ")
        count += 1
print("count=", count)

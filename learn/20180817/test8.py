import math

while True:
    num = int(input("input a num > "))
    if num <= 1:
        print("the number is not prime! please input the right number")
    isPrime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            isPrime = False
            break
    print("the num you input is prime: ", isPrime)

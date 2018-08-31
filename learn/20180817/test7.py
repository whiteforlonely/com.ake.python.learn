summary = 0
for i in range(5):
    multi = 1
    for j in range(i+1):
        multi *= (j+1)
    print("multi", i+1, "=", multi)
    summary += multi
print("sum=", summary)

temp = 1
summary = 0
for i in range(1, 6):
    temp *= i
    summary += temp
print("summary of 1..5!", summary)

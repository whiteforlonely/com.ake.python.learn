cmd = input("input a number or enter to exit")
average = 0
summary = 0
count = 0
while cmd:
    count += 1
    first = int(cmd)
    summary += first
    average = summary / count
    print("average:", average)
    cmd = input("input a number or enter to exit")

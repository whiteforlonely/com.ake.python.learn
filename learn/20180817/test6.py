while True:
    num = int(input("the score os student:"))
    result = "A"
    if num >= 90:
        result = "A"
    elif num >= 80:
        result = "B"
    elif num >= 70:
        result = "C"
    elif num >= 60:
        result = "D"
    else:
        result = "E"
    print("the student result is ", result)

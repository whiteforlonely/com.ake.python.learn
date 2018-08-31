feb = 1
feb2 = 1
summary = feb + feb2
i = 2
while True:
    feb = feb2
    feb2 = summary
    i += 1
    if i == 101:
        print(summary, end=" ")
        break

    summary = feb + feb2

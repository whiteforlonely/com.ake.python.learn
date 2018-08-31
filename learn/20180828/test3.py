def add(x=7, y=3):
    result = x + y
    return result


print(add())
print(callable(add))


def showconfig(**kwargs):
    for k, v in kwargs.items():
        print("{}={}".format(k, v))


showconfig(host="home", port="1024")

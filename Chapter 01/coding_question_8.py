x = 20
def function_1():
    global x
    x = 10
    return x
def function_2():
    return x

print(function_2())

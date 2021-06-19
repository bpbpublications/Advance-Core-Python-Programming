x = 20
def print_x():
    global x
    x = 10
    return x
print(print_x() )

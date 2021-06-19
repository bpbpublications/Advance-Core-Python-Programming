def funny(x,y):
    if y == 1:
       return x[0]
    else:
        a = funny(x, y-1)
        if a > x[y-1]:
            return a
        else:
            return x[y-1]
x = [1,5,3,6,7]
y = 3
print(funny(x,y))

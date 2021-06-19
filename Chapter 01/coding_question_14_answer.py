def funny(x,y):
    print("calling funny , y = ",y)
    if y == 1:
       return x[0]
    else:
        print("inside else loop because y = ", y)
        a = funny(x, y-1)
        print("a = ",a)
        if a > x[y-1]:
            print("a = ",a, " Therefore a > ",x[y-1])
            return a
        else:
            print("a = ",a, " Therefore a < ",x[y-1])
            return x[y-1]

x = [1,5,3,6,7]
y = 3
print(funny(x,y))


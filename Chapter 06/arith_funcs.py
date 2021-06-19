def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if(y==0):
        str1 = "zero not allowed as denominator"
        return str1
    else:
        return x/y

print(add(7,8))
print(subtract(5,6))
print(multiply(8,0))
print(divide(8,9))

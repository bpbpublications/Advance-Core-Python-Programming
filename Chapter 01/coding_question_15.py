def funny(x):
    if (x%2 == 1):
        return x+1
    else:
        return funny(x-1)
print(funny(7))    
print(funny(6))

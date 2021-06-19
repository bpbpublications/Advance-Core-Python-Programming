def n_power(n):
    if n < 0:
        print("please enter a positive value")
    elif n == 0:
        return 1
    else:
        return n_power(n-1)*3
print(n_power(4))

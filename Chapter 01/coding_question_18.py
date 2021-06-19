def even(k):
    if k <= 0:
        print("please enter a positive value")
    elif k == 1:
        return 0
    else:
        return even(k-1) + 2
print(even(6))

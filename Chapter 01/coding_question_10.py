def fibonacci_seq(num):
    i = 0
    j = 0
    k = 0
    for i in range(num):
        if i==0:
            print(j)
        elif i==1:
            j = 1
            print(j)
        else:
            temp = j
            j = j+k
            k = temp
            print(j)
fibonacci_seq(10)

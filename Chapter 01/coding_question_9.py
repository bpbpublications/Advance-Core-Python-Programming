def factorial(number):
    j = 1
    if number==0|number==1:
        print(j)
    else:
        for i in range (1, number+1):
            print(j," * ",i," = ",j*i)
            j = j*i
    print(j)
factorial(5)

def sum_func(a, *args):
    s = a+sum(args)
    print(s)

sum_func(10)
sum_func(10,20)
sum_func(10,20,30)
sum_func(10, 20, 30, 40)

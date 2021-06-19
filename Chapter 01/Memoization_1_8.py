def fibonacci(num):
    fib_num = [-1]*(num + 1)
    return fib_calculate(num, fib_num)
def fib_calculate(num, fib_num):
    if fib_num[num] >= 0:
        return fib_num[num]
    if (num<= 1):
        fnum = num
        return fnum
    else:
        fnum = fib_calculate(num - 1, fib_num) + fib_calculate(num - 2, fib_num)
        fib_num[num] = fnum
        return fnum

num = int(input('Enter the number: '))
print("Answer = ",fibonacci(num))

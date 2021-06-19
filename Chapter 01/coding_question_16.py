def fibonacci_seq(num):
    if num<0:
        print("Please provide a positive integer value")
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fibonacci_seq(num-1)+fibonacci_seq(num-2))

for i in range(10):

    print(fibonacci_seq(i))

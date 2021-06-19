def sum_prod(num1,num2):
    num_sum = num1 + num2
    num_prod = num1 * num2
    return num_sum,num_prod

x = int(input('Enter the first number :'))
y = int(input('Enter the second number :'))
print(sum_prod(x,y))

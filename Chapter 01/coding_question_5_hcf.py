def hcf(x,y):
    small_num = 0
    greater_num = 0
    temp = 0
    if x > y:
        small_num = y
        greater_num = x
    else:
        small_num = x
        greater_num = y

    while small_num > 0:
        temp = small_num
        small_num = greater_num % small_num
        greater_num = temp
    return temp


print("HCF of 6 and 24 = ",hcf(6,24))
print("HCF of 400 and 300 = ",hcf(400,300))

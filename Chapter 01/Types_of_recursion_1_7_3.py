def happy_new_year(n=1):
    if(n<=0):
        how_many_times()

    for i in range(n):
        print("Happy New Year")

def how_many_times():
    val = input("How many times should I print?:")
    if val=='':
        happy_new_year()
    else:
        happy_new_year(int(val))

        
how_many_times()

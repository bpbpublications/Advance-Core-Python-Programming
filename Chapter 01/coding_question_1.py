def create_substrings(x):
    substrings = []

    for i in range(len(x)):
        for j in range(1, len(x)+1):
            if x[i:j] != '':
                substrings.append(x[i:j])
    for i in substrings:
        check_palin(i)

def check_palin(x):
    palin_str = ''
    palin_list = list(x)
    y = len(x)-1
    while y>=0:
        palin_str = palin_str + palin_list[y]
        y = y-1
    if(palin_str == x):
        print("String ", x," is a palindrome")
    

x = "malayalam"
create_substrings(x)

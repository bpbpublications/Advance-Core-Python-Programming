# Default Argument
def n_power(n):
    if n < 0:
        print("please enter a positive value")
    elif n == 0:
        return 1
    else:
        return n_power(n-1)*3
print(n_power(4))




#Keyword Argument
def func(name1, name2):
    print("Happy Birthday", name1, " and ",name2,"!!!")

func(name2 = "Richard",name1 = "Marlin")



#Variable Length Argument
def func(*name, **age):
   print(name)
   print(age)
func("Lucy","Aron","Alex", Lucy = "10",Aron = "15",Alex="12")

x = int(input("Enter first number : "))
y = int(input("enter second number : "))
try:
    divide = x/y
    print("try block over")
    print("divide = ",divide)
except ZeroDivisionError:
    print("OOPS exception occured due to Zero division error")
    print("****THE END****")
####################################
    
#Example 6.4
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
except ZeroDivisionError:
print("OOPS exception occurred due to Zero division error")
print("****THE END****")
##############################################

a = int(input(“Enter first number : “))
b = input("enter second number : ")
try:
    divide = a/b
print("try block over")
print("divide = ",divide)
except (ZeroDivisionError,TypeError) :
print("OOPS exception occurred due to Exception")
print("****THE END****")
###################################################
a = int(input(“Enter first number : “))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
except (ZeroDivisionError,TypeError) :
    print("OOPS exception occurred due to Exception")
    print("****THE END****")
################################################

#6.3.2 Catching Exception in general
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
except TypeError as e:
    print(str(e))
####################################################
#Example 6.5
import sys
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception occurred due to ",sys.exc_info()[0])
    print("****THE END****")
###########################################################
#Example 6.6
import sys
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception occurred due to ",sys.exc_info()[1])
    print("****THE END****")

##################33
#Example 6.7
import sys
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception occurred due to ",sys.exc_info()[2])
    print("****THE END****")
###########################33
#Exaple 6.8
import sys
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("try block over")
    print("divide = ",divide)
#Access more information with sysexc_info
except:
    print("OOPS exception occurred due to line no.",sys.exc_info()[2].tb_lineno)
    print("****THE END****")
##############################################3
#16.3.3 Try … Except…else Statement
#Case 1 with exception, else block not executed
import sys
a = int(input("Enter first number : "))
b = input("enter second number : ")
try:
    divide = a/b
    print("divide = ",divide)
except:
    print("OOPS exception occurred due to line no.",sys.exc_info()[2].tb_lineno)
else:
    print("try over successfully")
    print("****THE END****")
#Case2 With no exception, else block executed
import sys
a = int(input("Enter first number : "))
b = int(input("enter second number : "))
try:
    divide = a/b
    print("divide = ",divide)
except:
    print("OOPS exception occurred due to line no.",sys.exc_info()[2].tb_lineno)
else:
    print("try over successfully")
    print("****THE END****")
###########################################
#6.3.4 Try…Except…Finally…..

def just_having_fun():
    try:
        print(4)
    except TypeError as e:
        print(str(e))
    finally:
        print("Ok Bye")

just_having_fun()
#######################################
try:
    voter_age = int(input("Enter the age of the voter : "))  
    if voter_age< 18:  	
        raise ValueError;
    else:
        print("You can vote")  
except ValueError:
    print("You are not allowed to vote")

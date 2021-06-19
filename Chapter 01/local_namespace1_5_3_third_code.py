x = 20
def print_x():
   global x
   x = 10
   print('Local variable x is  equal to ',x )

print('Global variable x is  equal to ',x )
print_x()
print('Global variable x is  equal to ',x )

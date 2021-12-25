#Write a Python program to create the colon of a tuple.

from copy import deepcopy
#create a tuple
hello = ("HELLO", 5, [], True) 
print(hello)
#make a copy of a tuple using deepcopy() function



hello_colon = deepcopy(hello)
hello_colon[2].append(50)
print(hello_colon)
print(hello)

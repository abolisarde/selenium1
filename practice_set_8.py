# 1.	Write a program using the function to find the greatest of three numbers.
# a = int(input("Enter the no.:"))
# b = int(input("Enter the no.:"))
# c = int(input("Enter the no.:"))

# def greatest():
#     if a>b :
#         if a>c:
#             print("a is greatest")
    
#     elif b>c:
#         print("c is greatest")
#     else:
#         print("c is greatest")
# greatest() 





# 2.	Write a python program using the function to convert Celsius to Fahrenheit.
# a= float(input("Enter tem. in celsius: "))
# def cel_to_fahr():
#     F = ((9/5)*a + 32)
#     print (F)

# cel_to_fahr()

# 3.	How do you prevent a python print() function to print a new line at the end?
# 4.	Write a recursive function to calculate the sum of first n natural numbers.
# 5.	Write a python function to print the first n lines of the following pattern.
# ***

# **       #For n = 3

# *
# n = 3
# def pattern():
#     for i in range (0,3):
#         for j in range (0,3-i):
#                 print("*",end="")
#         print()

# pattern()


# Copy
# 6.	Write a python function that converts inches to cms.
# 7.	Write a python function to remove a given word from a list and strip it at the same time.
 
# 8.	Write a python function to print the multiplication table of a given number.



# number=int(input("Enter an integer:"))
# def table():
    
#    for count in range (1,11):
#     product=number*count
#     print (number,"*",count,"=",product)
# table()



def greet(name):
     gr="hellow" + name
     return gr
a= greet("Aboli")
print(a)
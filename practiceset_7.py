# 1.	Write a program to print the multiplication table of a given number using for loop.
# iCounter = 1
# while iCounter<=10:
#     print(5 * iCounter )
#     iCounter=iCounter+1

# iCounter =1
# for i in range(0,10):
#         print(5 * iCounter)
#         iCounter = iCounter+1



# 2.	Write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 = ["HARRY","Sohan","Sachin","Rahul"]
# check ="S"
# for i in l1:
#     if(i.find(check)):
#         print(l1)
# Copy
# 3.	Attempt problem 1 using a while loop.
# 4.	Write a program to find whether a given number is prime or not.
# number = int(input("Enter the no. :"))
# if number > 1:
#     for i in range(2,number):
#         if number % i == 0 :
#             print("number is not prime ",number)
            
#             break
#         else :
#              print("number is prime ",number)

# 5.	Write a program to find the sum of first n natural numbers using a while loop.
# number = int(input("Enter the no. :"))
# if number < 0:
#     print("Enter the positive number")
# else:
#     sum = 0
# while (number > 0):
#     sum += number
#     number -= 1
#     print("the sum is ", sum)

# 6.	Write a program to calculate the factorial of a given number using for loop.
# number = int(input("Enter the no. :"))
# factorial = 1

# for i in range(1,number + 1):
#         factorial = factorial * i
# print("factorial of",number,"is",factorial)
    

# 7.	Write a program to print the following star pattern.

#     *

#   ***  

# ***** for n=3

# n = 3
# for i in range (0,3):
#     for j in range(0, 2*i+1):
#      print("*",end='') 
#     print()                                                                                                                                                              
          
# Copy
# 8.	Write a program to print the following star pattern:
# *

# **

# *** for n = 3

# n = 3
# for i in range (0,3):
#     for j in range(0 , i+1):
#      print("*",end='')
#     print()
# Copy
# 9.	Write a program to print the following star pattern:
# * * *
# *   *             #For n=3
# * * * 
# Copy



#    10. Write a program to print the multiplication table of n using for loop in reversed order.
# 
# table = int(input("Enter the table:"))
# limit = int(input("Enter the ending"))
# for i in range (limit,0,-1):
#         print(i,"*",table,"=",i*table)



# number = int(input("Enter tne no."))
# if number>1:
#         for i in range(2,number):
#                 if number % i ==0:
#                         print("not prime")
#                 else:
#                         print("prime")

a=0
b=1
for i in range (1,10):
        c=a+b
        a=b
        b=c
print(b)







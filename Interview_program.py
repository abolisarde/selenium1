# 1. Write a program to swap two numbers.
# a = int(input("Enter the no:"))
# b = int(input("Enter the no:"))

# temp = a
# a = b
# b = temp

# print("The value of a after swapping:", a)
# print("The value of a after swapping:", b)

#2. How to check number is prime or not.
# n = int(input("Enter the no:"))
n =[10,15,88,15,33,11,77]
alist = list(filter(lambda x:(x%2+1==0),n))
print(alist)
# if n>1:
#     for i in range (2,int(n/2)+1):
#         if (n % i) ==0:
#             print("no.is not prime")
#             break
#         else:
#             print("no.is prime")



# 3. How to find factorial of a number

# number = int(input("Enter the number :"))
# factorial = 1
# if number < 0 :
#     print ("Factorial does not exist negative number")
# elif number == 0 :
#     print("factorial of 0 is 1")
# else:
#     for i in range (1,number+1):
#         factorial = factorial*i
#     print("The factorial of ",number, "is",factorial)    
# 
# 
# 
#  6. How to find maximum and minimum elements in an array? 
# array = [10,15,88,15,33,11,77]
# result = array.sort()
# print("Greatest element is:",array[-1])

# result2 = array,(reversed==True)
# print("Smallest element is:",array[0])




# 4. Print Fibonacci series.

# 5. How to find the sum of elements in an array?

# array = [10,15,88,15,33,11,77]
# sum = 0

# for i in range (0 , (len(array))) :
#     sum = sum + array[i]
# print (sum)    

# 7. How to find the length of the list?
# aList = [15,26,77,63,1,0,5,8,98,100]
# print(len(aList))

# 8. How to swap first and last elements in the list
# aList = [15,26,77,63,1,0,5,8,98,100]
# print("After swapping list:",aList)

# aList[0],aList[9] = aList[9],aList[0]
# print("swapping list:",aList)


# 9. How to swap any two elements in the list?
# aList = [15,26,77,63,1,0,5,8,98,100]
# print("After swapping list:",aList)

# aList[3],aList[6] = aList[6],aList[3]
# print("swapping list:",aList)


# 10. How to remove the Nth occurrence of a given word list? 
 

# 11. How to search an element in the list?
# List = [15,26,77,63,1,0,5,8,98,100]


# for i in List:
#     if (i==77):

#        print("Element is in list")

   
   

# 12. How to clear the list?
# aList = [15,26,77,63,1,0,5,8,98,100]
# print(aList.clear())
# print("clear list",aList)

# 13. How to reverse a list?
aList = [15,26,77,63,1,0,5,8,98,100]
# aList.reverse()
# print("Reverse the list :",aList)
result =aList[::-1]
print(result)

# 14. How to clone or copy a list?
# aList = [15,26,77,63,1,0,5,8,98,100]
# bList = aList.copy()

# print("aList copy in bList:",bList)

# 15. How to count occurrences of an element in a list?
# aList = [15,26,77,63,1,0,5,8,98,100,15,True,15]
# countList = aList.count(15)
# print("count of list is :",countList)


# from functools import reduce
# # 16. Find the sum of the elements in list
# List = [15,26,77,63,1,0,5,8,98,100,15,15]
# sum = 0
# for i in List:
#     sum = sum + i
# print("sum of list elements is :",sum)    
# listsum = reduce(lambda a,b : a+b,List)
# print(listsum)




# 17. How to multiply all the numbers in the list?

# from functools import reduce

# list = [5,6,12,14,8,22,10,7]

# listmulti = reduce(lambda a,b : a*b,list)
# print ("Multiplication of all no is :",listmulti)

#  18. How to find the smallest and largest numbers on the list?
# aList = [15,26,77,63,1,0,5,8,98,100]
# # smallest = min(aList)
# # largest = max(aList)
# # print("smallest no in list:",min(aList))
# # print("largest no in list :",max(aList))

# aList.sort()
# print(aList)
# print("smallest no in list:",aList[0])
# print("smallest no in list:",aList[-1])


# 19. How to find the second-largest number in a list?
# aList = [15,26,77,63,1,0,5,8,98,100]
# aList.sort()
# print("second largest no:",aList[-2])

# 20. How to check string is palindrome or not?
# string = "madam"
# string = input("Enter string")
# string1 = ""

# for i in string:
#      string1 = i + string1
# if string == string1:
#         print("it is pallidrome")
# else:
#         print("not pallidrome")    

# 21. How to reverse words in a string?
string = "Abhimanyu is my baby"
words = string.split(' ') [::-1]
l=[]
for i in words:
    l.append(i)
print("".join(l))


# 22. How to find a substring in a string?
# str = "Abhimanyu is good boy"
# result = str.find("is")
#
# if result !=2:
#     print ("not present")
# else:
#     print("present")


# 23. How to find the length of a string?
# aValue = "Abhimanyu"
# print(len(aValue))

# 24. How to check if the string contains any special character?
# str = "aboli@*girl"
# str = input("enter the string")

# # str.split()
# a = '[!@#$%^&*]'
# c = 0
# for i in range(len(str)):
#     if str[i] in a:
#         c=c+1
# if c>0:
#     print("present")
# else:
#     print("not present")            
 

# 25. Check for URL in a string
# string = "this is my url https//www.google.com"
# c = []
# x = string.split()
# for i in x:
#  if i.startswith('https'):
#     c.append(i)
# print(c)        


# alist =[1,5,4,88,99,12,10,11,35,77]
# newlist=list(filter(lambda x:(x%2==0),alist))
# print(newlist)
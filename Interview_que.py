# #
# # 1. Write a program to swap two numbers.
# a =30
# b =40
# a,b =b,a
# print('swapping of a:', a)
# print('swapping of b:', b)
#
# # # 2. How to check number is prime or not.
# n = int(input("Enter the no:"))
# if n>1:
#     for i in range(2,int(n/2)+1):
#         if n % i==0 :
#             print("no.is not prime")
#         else:
#             print("no is prime")




#
#
 # 3. How to find factorial of a number
#
#
# # n = int(input("Enter the no:"))
# # factorial = 1
# # for i in range(1,n+1):
# #  factorial=i*factorial
# # print(factorial)
#
#
# # 6. How to find maximum and minimum elements in an array?
# # Array=[1,5,7,88,44,1,5,44,68,70]
# # print(max(Array))
# # print(min(Array))
#
# # 16. Find the sum of the elements in list
# Alist = [3, 15, 45, 88, 47, 66, 5, 1]
# # sum=0
# #
# # for i in range(0,(len(Alist))):
# #     sum=sum+Alist[i]
# # print(sum)
# #
# # from functools import reduce
# # sum=reduce(lambda a,b:a+b,Alist)
# # print(sum)

 # 4. Print Fibonacci series.
#  n1=0
#  n2=1
#  count=0
#  print(n1)
#  print(n2)
#
# for i in range(2,10):
#      sum=n1+n2
#      print(sum)

value = int(input("Enter age"))
if value >=18:
    print("yes")
else:
    print("no")




# # 5. How to find the sum of elements in an array?
# #
# # # 7. How to find the length of the list?
# Alist = [3, 15, 45, 88, 47, 66, 5, 1]
# # print(len(Alist))
# # #
# # 8. How to swap first and last elements in the list
# # Alist[2],Alist[5]=Alist[5],Alist[2]
# # print(Alist)
# # 9. How to swap any two elements in the list?
# #
# # 10. How to remove the Nth occurrence of a given word list?
# Alist.remove(88)
# print(Alist)
#
# #
# # 11. How to search an element in the list?
# # Alist = [3, 15, 45, 88, 47, 66, 5, 1]
# # ele = 88
# # for i in Alist:
# #     if i == 88:
# #         print("element is present")
# # else:
# #     print("element is not present")
#
# #
# # # 12. How to clear the list?
# # Blist=[1,2,4,5,7,8,9,40]
# # Blist.clear()
# # print(Blist)
# # # 13. How to reverse a list?
# # Alist.reverse()
# # print(Alist)
# # # 14. How to clone or copy a list?
# # Blist=Alist.copy()
# # print(Blist)
# #
# # 15. How to count occurrences of an element in a list?
# #
# # 17. How to multiply all the numbers in the list?
# from functools import reduce
# alist =[1,2,5]
# result =reduce(lambda a,b:a*b,alist)
# print(result)

# 18. How to find the smallest and largest numbers on the list?
# alist =[1,2,5,77,52,8,22]
# alist.sort()
# print(alist[0])
# print(alist[-1])
# # 19. How to find the second largest number in a list?
# alist =[1,2,5,77,52,8,22]
# result = alist.sort()
# print(alist[-2])

# # 20. How to check string is palindrome or not?
string = "madam"
string1 = ""
for i in string:
    string1 = i + string1
if string==string1:
        print("is palendrome")
else:
        print("not palendrome")

# # 21. How to reverse words in a string?
# str ="Abhimanyu is my Boy"
# word =str.split(' ') [::-1]
# l =[]
# for i in word:
#     l.append(i)
# print("".join(l))

# # 22. How to find a substring in a string?
# str ="Abhimanyu is my Boy"
# result = str.find("is")
# if result !=2:
#     print("substeing  not is present")
# else:
#     print("substring not present")


# # 23. How to find the length of a string
# blist = "aboli@4555"
# print (len(blist))
# #
# # 24. How to check if the string contains any special character?
# blist = "aboli@4555"
# blist.split()
# a ='[!,@,#,$,%,^,&,*]'
# c=0
# for i in range (len(blist)):
#     if blist[i]in a:
#         c=+1
# if c>0:
#         print('present')
# else:
#         print('Absent')



# # 25. Check for URL in a string
# string = "This is my url https://www.google.com"
# c = []
# x = string.split()
# for i in x:
#     if i.startswith('https'):
#         c.append(i)
# print(c)

n =5
for i in range (n):
    for j in range (n-i-1):
        print('',end='')
    for k in range (2*i+1):
        print('* ',end='')
    print()



# # Chapter 6 – Practice Set
# # 1.	Write a program to find the greatest of four numbers entered by the user.
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if a>b:
#     if a>c:
#         if a>d:
#             print(a)
#         else:
#             print(d)
#     else:
#         if c>d:
#             print(c)
#         else:
#             print(d)
# else:
#     if b>c:
#         if b>d:  
#            print(b)
#         else:
#             print(d)
#     else:
#         if c>d:
#             print(c)
#         else:
#             print(d)


         
# # 2.	Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# t(a+b+c)







# # 3.	A spam comment is defined as a text containing the following keywords:
# # “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.




# # 4.	Write a program to find whether a given username contains less than 10 characters or not.
# name = input("Enter your name")
# if(len(name)<10):
#     print("Your user name is correct")
# else:
#     print("Your user name is not correct")




# # 5.	Write a program that finds out whether a given name is present in a list or not.
# namelist=['Aboli','vivek','Abhimanyu','OM','Audu','Ganesh','Rani','Adarsh']
# name=str(input("enter your name"))
# if name in namelist:
#     print("name present in list")
# else:
#     print("name is not present in list")    





# # 6.	Write a program to calculate the grade of a student from his marks from the following scheme:
# # 90-100	Ex
# # 80-90	A
# # 70-80	B
# # 60-70	C
# # 50-60	D
# # <50	F
# aValue=int(input("Enter your marks:"))
# if aValue>=90  and aValue<=100:
#     print("Your Grade is Ex")
# elif aValue>=80 and  aValue<=90:
#     print("Your Grade is A")
# elif aValue>=70 and  aValue<=80:
#     print("Your Grade is B")
# elif aValue>=60 and  aValue<=70:
#     print("Your Grade is C")
# elif aValue>=50 and  aValue<=60:
#     print("Your Grade is D")
# elif aValue<=50:
#     print("your Grade is F")
    
        









# # 7.	Write a program to find out whether a given post is talking about “Harry” or not.
# post = input("Enter the post:")
# if ("Harry"in post):
#                      print("Yes,the post contain Harry")
# elif("harry"in post):
#     print("Yes,the post contain harry")
# else:
#     print("No,the post not contain Harry")   

 


n = 1
while(n<=50):
    print(n)
    n+=1
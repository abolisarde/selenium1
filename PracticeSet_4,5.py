# # 1.	Write a program to store seven fruits in a list entered by the user.

# # fruitslist = ['Apple','Mango','Banana','Grapes','Orange','Strawberry','Chiku']
# # print(fruitslist[4])




# # 2.	Write a program to accept the marks of 6 students and display them in a sorted manner.

# # marks=[75,89,69,88,98,77]
# # sorted=marks.sort()
# # print(f"marks in sorted manner{marks}")



# # 3.	Check that a tuple cannot be changed in Python.
# # aTupleVariable = (10, 20, 80, 30,15)
# # print(aTupleVariable[2])        ##80
# # (aTupleVariable[2])=50           ##TypeError: 'tuple' object does not support item assignment



# # 4.	Write a program to sum a list with 4 numbers.
list = [1,5,8,6]                            # 20
# print("the sum of list is:",sum(list))
sum=0
for i in list:
    sum=sum+i
print(sum)


# # 5.	Write a program to count the number of zeros in the following tuple:
# # a = (7, 0, 8, 0, 0, 9)

# # print(a.count(0))


######================== Practice set 5 ==================================



#  1.	Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!
# 2.	Write a program to input eight numbers from the user and display all the unique numbers (once).
# n= int(input("enter no of elements:"))
# unique_no= list (set(n))
# print(unique_no)


# 3.	Can we have a set with 18(int) and “18”(str) as a value in it?  #yes {18, '18'}
# 4.	What will be the length of the following set S:
# S = {18,"18",3,5}
# print(S)        ##TypeError: set expected at most 1 argument, got 4


# S = set()
# S.add(20.0)
# S.add(20)

# S.add("20")
# print(len(S))

# # Copy
# What will be the length of S after the above operations?
# # 5.	
S = {}#, what is the type of S?
print(type(S))
# # 6.	Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
dict= {
    'Marathi':'Aboli',
    'English':'Vivek',
    'urdu':'Om',
    'kanad':'audu',
    'English':'Ganesh',
    'urdu':'audu'
}
# print(dict)
# 7.	If the names of 2 friends are the same; what will happen to the program in Program 6?
# 8.	If the languages of two friends are the same; what will happen to the program in Program 6?
# 9.	Can you change the values inside a list which is contained in set S
#### set items are unchangeable,meaning that we cannot change items after the set has been created
# S = {8, 7, 12, “Harry”, [1, 2]}

list=[1,2,3,5,6,7]
a=0
while(a<len(list)):
    print(list[a])
    a=a+1

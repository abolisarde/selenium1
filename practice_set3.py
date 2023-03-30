# # 1.	Write a program to detect double spaces in a string. (count of double space or count of any char)
# # aValue=''' Dear  Candidate, 
# # We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# # Thank you,  '''
# # print(aValue.count("  "))

# # 2.	Write a program to format the following letter using escape sequence characters.

# # Dear  Candidate, 
# # 	We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# # Thank you,

# # 3.	From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function

# # Letterformat = "    \n Dear  Candidate, \n    We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us. \n  Thank you, \n  HR"
# # Offerletter = Letterformat.replace("Candidate","Aboli").replace("HR"," HR Sagar Sir")
# # #print(Offerletter)

# # print(f"old value {Letterformat} : new value after replace {Offerletter}")


# # # 4.	Replace the double spaces from problem 3 with single spaces.

# aValue =''' Dear  Candidate, 
# 	We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# Thank you,'''

# print(aValue.replace("  ","   "))



# name="HarryisGood"
# d= name[0::2]          #Hrysod
# print(d)



# age =int(input("age user entered:"))
# if (age>=18):
#  print("your age is 18+")
# else:
# 	print("you are not yet18 ")



# 1.	Write a Python program to display a user-entered name followed by Good Afternoon using input() function

# aValue = str(input("Enter ur name:"))
# print("Good Afternoon ")



#2.	Write a program to fill in a letter template given below with name and date.
letter = ''' Dear <|NAME|>,

                       You are selected!

                        <|DATE|>'''


name =input ("Enter ur name :")
date = input("Enter date")
letter = letter.replace('<|NAME|>',name)
letter = letter.replace('<|DATE|>',date)

print(letter )
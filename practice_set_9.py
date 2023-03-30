# 1.	Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.

# file = r"C:\Users\omipa\OneDrive\Documents\poem.txt"
# with open(file,'r') as  firstfile :
#  text = firstfile.read()
#  print(text)


# def search_str (file, word):
#     with open(file,'r') as  firstfile :
#      text = firstfile.read()
#      if word in text:
#         print("string exist in file")
#      else:
#         print("string does not exist in file")
# search_str(r'C:\Users\omipa\OneDrive\Documents\poem.txt','twinkle')




# 2.	The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
# 3.	Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13- year old boy.
# 4.	A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

a = input("Enter the text:")
file = open (r'C:\Users\omipa\OneDrive\Documents\poem2.txt','r+')
l = file.readlines()
file.write(a)
file.close()
print("text successfully replced :")

# 5.	Repeat program 4 for a list of such words to be censored.
# 6.	Write a program to mine a log file and find out whether it contains ‘python’.
# 7.	Write a program to find out the line number where python is present from question 6.
# 8.	Write a program to make a copy of a text file “this.txt.”

# with open('poem2.txt','r') as firstfile, open ('poem.txt','w') as secondfile :
#  for line in firstfile :
#     secondfile.write(line)
# 9.	Write a program to find out whether a file is identical and matches the content of another file.

# import filecmp
# f1 = r"C:\Users\omipa\OneDrive\Documents\poem.txt"
# f2 = r"C:\Users\omipa\OneDrive\Documents\poem2.txt"

# resut = filecmp.cmp(f1 , f2, shallow=True)
# print(resut)
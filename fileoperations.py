# File reading operation 

# Go to file path or folder and locate file with file name
# Open file
# Read content/write content to file
# Save file if you made changes
# copy content you got from file and use it
# Close


try:
 filevariable = open(r"C:\Users\omipa\OneDrive\Documents\file operations.txt")
 filecontent = filevariable.read()

 print("File content:", filecontent)
except Exception as e:
    print (e)
finally:
    try:

     filevariable.close()
    except Exception as e:
        print("File never opened")


# ##=================================

# filepath = r"C:\Users\omipa\OneDrive\Documents\file operations.txt"
# with open (filepath,'r+')as filevariable:
#     filecontent = filevariable.read()
#     print(filecontent)


## file will be automatically closed with block will complete execution with or without exception.



# filepath = r"C:\Users\omipa\OneDrive\Documents\file operations.txt"
# filecontent = 'welcome to ct12 batch'
# with open (filepath,'w')as filevariable:
#      temp = filevariable.write(filecontent)
#      print(filecontent)
#      print(temp)


# filepath = r"C:\Users\omipa\OneDrive\Documents\file operations.txt"
# with open (filepath,'r+') as filevariable :
#     filecontent = filevariable.read()
#     print(filecontent)






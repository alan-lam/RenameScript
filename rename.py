#! python3

import os

currDir = os.getcwd()

print("Press Ctrl+C to exit")
print("Enter 1 to rename files only")
print("Enter 2 to rename folders only")
choice = input("Press any key to rename everything: ")
remove = input("Enter word/char to remove from file/folder name: ")
replace = input("Enter word/char to replace: ")

fileFlag = True
folderFlag = True

if choice == str(1):
    folderFlag = False
elif choice == str(2):
    fileFlag = False

for foldername, subfolder, filenames in os.walk(currDir):
    if fileFlag == True:
        for filename in filenames:
            if filename == "rename.py" or filename == "rename.bat":
                continue
            name, ext = os.path.splitext(filename)
            listy = name.split(remove)
            newName = replace.join(listy)
            os.rename(filename, newName + ext)
    if folderFlag == True:
        for folder in subfolder:
            if remove in folder:
                newName = folder.replace(remove, replace)
                os.rename(folder, newName.strip())


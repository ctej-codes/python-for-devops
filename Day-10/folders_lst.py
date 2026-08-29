import os

folders_lst = input("Enter the folder names seperated by a space: ").split()

for folder in folders_lst:
    try:
        files = os.listdir(folder)
        print ("======Printing the files in folder: ", folder)
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Enter a valid folder name", "as", folder, "is not found")
    ece
        continue
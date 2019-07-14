# My solution
# from datetime import datetime
# file1 = open("file1.txt" , "r")
# content1 = file1.read()
# file2 = open("file2.txt", "r")
# content2 = file2.read()
# file3 = open("file3.txt", "r")
# content3 = file3.read()
# now = datetime.now()
#
# timeNow = now.strftime("%Y-%m-%d-%H-%M-%s-%ms")
# file4 = timeNow + ".txt"
# with open(file4, "w") as myFile:
#     myFile.write(content1 + '\n')
#     myFile.write(content2 + '\n')
#     myFile.write(content3 + '\n')

#A better recommended solution
import glob2
from datetime import datetime
#generate list of fileNames ending with .txt
fileNames = glob2.glob("*.txt")
fileNames.sort()
#This is to write to file
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    #Iterate through the list of file names
    for filename in fileNames:
        #In order to write in file, we first have to read the files in filenames
        with open(filename, "r") as f:
            #After reading, write to file names
            file.write(f.read() + "\n")

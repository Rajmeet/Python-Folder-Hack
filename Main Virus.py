import os


#Creating Multiple folders
def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Making Directory..." + directory)

#Virus Creation
"""
i = 1
while True:
    if(i > 0):
        print("Hello")
"""

a = range(0,10)
for x in a:
    print(str(x))
createFolder(x)
 No newline at end of file
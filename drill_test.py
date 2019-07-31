import os
import time 
fName = 'drill_test.txt'

fPath = 'C:/Users/Anders/Desktop/Bootcamp/Python/drill_test'

abPath = os.path.join(fPath,fName)
print(abPath)

dirs = os.listdir()
for file in dirs:
    if file.endswith('.txt'):
        print (file)
        
        mpath = os.path.join(fPath,file)
        
        mtime = time.ctime(os.path.getmtime(mpath))
        "time.ctime switches to"
        print(mtime)
    

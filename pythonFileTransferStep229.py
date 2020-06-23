import shutil
import os
import time

# Get current directory and contents of subfolder Source
current = os.getcwd()
fileList = os.listdir(current + "/Source")

# Get current time
curTime = time.time()

# Set 24-hour lag
dayAgo = curTime - 3600*24

# Cycle through files in subfolder, and check .txt files to see
# if they have been modified in the last day, and if so, move them to
# Destination subfolder, notify console.
for fileName in fileList:
    if fileName.endswith(".txt"):
        modifiedTime = os.stat(current + "/Source/" + fileName).st_mtime
        if modifiedTime > dayAgo:
            shutil.move(current + "/Source/" + fileName, current + "/Destination")
            print( "moved: " + fileName)




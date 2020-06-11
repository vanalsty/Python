import os
import os.path,time

from datetime import datetime

src = "C:\\PythonStep159"  ## or whatever your source directory is

sourceFiles = os.listdir(src) ## makes a list of all file names to iterate through
for file in sourceFiles:
    if file.endswith(".txt"):
        abPath = os.path.join(src, file)
        print(abPath)
        modTime = datetime.fromtimestamp(os.path.getmtime(abPath))  ## this fromtimestamp bit converts time since the epoch to something that is a bit more readable / has meaning to us
        print(modTime)

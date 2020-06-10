import os
import datetime
import os.path,time

from os import listdir
from os.path import isfile, join
path = "C:\\PythonStep159"
onlyTxtFiles = [f for f in listdir(path) if isfile(join(path, f)) and  f.endswith(".txt")]
print(onlyTxtFiles)



print("Last Modification:%s"%time.ctime(os.path.getmtime("C:\\PythonStep159\\anotherOne.txt")))

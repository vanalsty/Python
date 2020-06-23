import shutil
import os
import time

#set where the source of the files are
source = '/Users/lauri/Desktop/FolderA/'

#set destination
destination = '/Users/lauri/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)


# reference: www.geeksforgeeks.org/python-sort-and-store-files-with-same-extension/
import os
import shutil
   
# Write the name of the directory here,
# that needs to get sorted
path = 'Downloads'
  
  
# This will create a properly organized 
# list with all the filename that is
# there in the directory
list_ = os.listdir(path)
for file_ in list_:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
  
    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)

from tkinter import Tk, filedialog
import os
import shutil
def pysort():  
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_file = filedialog.askdirectory()
    print(open_file)
    path = open_file
  
  
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
    print("Sorting complete")

pysort()
print("Do you want to continue?")
ch = input()
while ch =='y':
    pysort()
    print("Do you want to continue?")
    ch = input()
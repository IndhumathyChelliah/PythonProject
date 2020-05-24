import os
#get current working directory
print (os.getcwd())
#changing directory
os.chdir('C:\indhuProject\pyhomework\datetime,pdb,timeit')
print (os.getcwd())
#list the files in the path-> returns in list format.
print (os.listdir())
#create new directory-one level deep
#os.mkdir("os-demo")
#create new directory many level deep
#os.makedirs("os/os_demo1")
#remove dir one level deep
#os.rmdir("os-demo")
#os.removedirs("os/os_demo1")
print (os.listdir())
#renaming files
#os.rename("d1.py","d2.py")
#get in formation about the file
print (os.stat("d2.py"))
#file modified time
from datetime import datetime
mod_time=os.stat("d2.py").st_mtime
#modified timestamp in human readable format
print (datetime.fromtimestamp(mod_time))
#os.walk() -is a generator that yields atuple of 3 values -dir path, dir within the path 
# and files within the directory
g=os.walk('C:\indhuProject\pyhomework\importingstatement')
for dirpath,dirnames,filenames in g:
    print ("Current path:",dirpath)
    print("Current directory: ",dirnames)
    print("filenames :",filenames)
    print()
print (os.environ.get("USERPROFILE"))
print (os.path.basename('C:\indhuProject\pyhomework\importingstatement')) 
print (os.path.dirname('C:\indhuProject\pyhomework\importingstatement')) 
print (os.path.split('C:\indhuProject\pyhomework\importingstatement')) 
'''
os.path.isdir()
os.path.isfile()
os.path.exists()
splits the extansion
os.path.splittext()
'''









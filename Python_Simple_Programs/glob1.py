import os,glob

os.chdir(r"C:\indhuProject\pyhomework\regular_expression")
for file in glob.glob("*.jpg"):
    print (file)


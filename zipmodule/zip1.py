import zipfile

'''
with zipfile.ZipFile('files.zip','w',compression=zipfile.ZIP_DEFLATED) as my_file:
    my_file.write('hello.txt')
    my_file.write('hi.txt')

 '''
 
with zipfile.ZipFile('files.zip','r') as my_file:
    #print(my_file.namelist())
    #my_file.extractall()
    my_file.extractall('files')


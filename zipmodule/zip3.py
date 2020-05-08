import requests
import zipfile

r=requests.get('https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U')

with open('data.zip','wb') as f:
    f.write(r.content)


with zipfile.ZipFile('data.zip','r') as data_zip:
    print (data_zip.namelist())



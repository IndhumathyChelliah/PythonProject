
import requests

r=requests.get('https://xkcd.com/353/')

#response success or not. 
print (r)
#print unicode text
#print (r.text)

#prints bytes from the image
r1=requests.get('https://imgs.xkcd.com/comics/python.png')
#print (r1.content)

'''
r1=requests.get('https://imgs.xkcd.com/comics/python.png')
with open ('c1.png','wb') as f:
    f.write(r1.content)
    '''
print (r1.ok)
print (r1.status_code)





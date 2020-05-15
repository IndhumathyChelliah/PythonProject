import requests
'''
r=requests.get('https://httpbin.org/get?page=2&count=25')
print (r.text)
'''
'''
payload={'page':2,'count':25}
r=requests.get('https://httpbin.org/get',params=payload)
print (r.url)
print (r.text)
'''
payload1={'username':'karthi','password':'karthi'}
r1=requests.post('https://httpbin.org/post',data=payload1)
#print (r1.text)
r_dict=r1.json()
print (r_dict['form'])
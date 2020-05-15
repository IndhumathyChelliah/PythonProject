import requests

r=requests.get('https://httpbin.org/basic-auth/karthi/karthi',auth=('karthi','karthi'))

print (r.text)
print (r)

r=requests.get('https://httpbin.org/basic-auth/karthi/karthi',auth=('karthi',''))
print (r)

r=requests.get('https://httpbin.org/delay/1',timeout=3)
print (r)

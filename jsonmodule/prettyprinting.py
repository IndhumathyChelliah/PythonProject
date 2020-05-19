import requests
from pprint import pprint

url="https://pypi.org/pypi/sampleproject/json"

r=requests.get(url)

pprint (r.json())
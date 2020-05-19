from tabulate import tabulate

data=[('indhu',25,'chennai'),('karthi',7,'nellai'),('sarvesh',3,'dindugal')]

headers=['Name','age','city']

print (tabulate(data,headers=headers,tablefmt='grid'))
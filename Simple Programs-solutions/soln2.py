

class dict_process:

    def __init__(self,fname,lname,age,fullname,address,skillset):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.fullname=fullname
        self.address=address
        self.skillset=skillset

    
    @classmethod

    def d_process(cls,dict):
        fname=dict['fname']
        lname=dict['lname']
        age=dict['age']
        fullname=dict['fullname']
        address=dict['address']
        skillset=dict['skillset']
        return dict_process(fname,lname,age,fullname,address,skillset) 

dict={'fname': 'indhu', 'lname': 'mathy', 'age': 25, 'fullname': 'indhu mathy', 'address': {'city': 'chennai', 'state': 'TN', 'zip': '627117'}, 'skillset': ['Python', 'SQL', 'Tableau', 'AWS']}
s=dict_process.d_process(dict)
print (s.address)










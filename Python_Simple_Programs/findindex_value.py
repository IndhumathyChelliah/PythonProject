def findindex(to_search,target):
    for i,value in enumerate(to_search):
        if value==target:
            return i
    else:
        return -1

to_search=['indhu','mathy','karthi','sarvesh','palani']
print (findindex(to_search,"indhu") )       

            

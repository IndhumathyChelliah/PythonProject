
from collections import Counter
with open("hello.txt","r")as f:
    f1=f.read()
    word=f1.split()
    print (word)
    #using Counter method
    c=Counter(word)
    print (sum(c.values()))

    #using for loop
    count=0
    for i in word:
        count+=1
    print (count)

    #using len function
    print (len(word))    
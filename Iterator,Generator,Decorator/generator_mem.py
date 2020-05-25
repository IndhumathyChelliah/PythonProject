import memory_profiler as mp
import random
import time

name=['indhu','mathy','karthi','sarvesh','palani']

print (f"Memory before:{mp.memory_usage()}mb ")
def normal(num):
    result=[]
    for i in range(num):
        person={
        id:i,
        'name':random.choice(name)
        }
        result.append(person)
    return result

def gen(num):
    for i in range(num):
        person={
        id:i,
        'name':random.choice(name)
        }
        yield person
'''    
t1=time.time()
normal(100000)
t2=time.time()
 '''   
t1=time.time()
gen(100000)
t2=time.time()

print (f"Memory before:{mp.memory_usage()}mb ")
print(f"took {t2-t1} seconds")


import random
#prints number between o and 1
print (random.random())
#prints random float number between 1 and 10
print(random.uniform(1,10))
#prints random integer between 1 and 10[includes 1 and 10]
print(random.randint(1,10))
l1=[1,2,3,4,5]
#prints one random element  from the list
print(random.choice(l1))
#returns list of random no of results mentioned in the key value
print(random.choices(l1,k=2))
# will shuffle the list
random.shuffle(l1)
print (l1)
deck=list(range(53))
# returns only unique values 
hand=random.sample(deck,k=5)
print (hand)
# choices method wont return unique values
hand1=random.choices(deck,k=5)
print(hand1)
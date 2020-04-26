
import itertools

letters=['a','b','c']
numbers=[1,2]


#combinations --> order does not matter
result=itertools.combinations(letters,2)
print (list(result))

#permutation --> order does matter
result1=itertools.permutations(letters,2)
print (list(result1))

#itertools.product  -> repeated value is allowed and order does matter
result2=itertools.product(numbers,repeat=3)
print(list(result2))

#combinations_with_replacement -> allows repeated value and orde does not matter

result3=itertools.combinations_with_replacement(numbers,3)
print (list(result3))






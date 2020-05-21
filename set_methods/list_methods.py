l1=[1,2,3]

#append
l1.append([4,5])
print ("Appended: {}".format(l1))
#clear
l1.clear()
print ("Cleared the list: {}".format(l1))
#copy
import copy
l1=[1,2,3,[4,5]]
l2=l1.copy()
print ("Copied : {}".format(l2))
l3=copy.deepcopy(l1)
print ("Deep Copied: {}".format(l3))
#count

#index
print (l1[0])
#extend
l4=[1,2,3]
l5=[4,5,6]
l4.extend(l5)
print (l4)
#insert
#list.insert(index,element)
l4.insert(0,0)
print (l4)
#pop(it will remove the last element in the list).
#if index is mentioned 

l4.pop()
print (l4)

#remove-it will remove the element 3 from the list
l4.remove(3)
print (l4)
# delete -> mention the index or slicing
del l4[1:]

#reverse
l4.reverse()
print (l4)
#sort
l4.sort()
print (l4)


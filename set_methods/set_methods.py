
#set methods

s1={1,2,3,4,5}

#add-to add one element
s1.add(6)
print (s1)

#update- to add more elements , to update elements from other set
s1.update([6,7,8])
print (s1)
s2=[9,10]
s1.update([8,9,11],s2)
print (s1)

#remove -> remove element, if it is not present, throws error
s1.remove(2)
#discard -> removes element , if it is not present, dont throw error
s1.discard(4)
s1.discard(4)

class A:
    def display(self):
        print ("This belongs to Class A")
class B(A):
    def display(self):
        print ("This belongs to Class B")

b=B()
b.display()
a=A()
a.display()

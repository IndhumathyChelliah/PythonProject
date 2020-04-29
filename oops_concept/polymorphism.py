
class Dog:
    def sound(self):
        print ("bow bow")
class Cat:
    def sound(self):
        print ("meow meow")
def AnimalSound(animaltype):
    animaltype.sound()

d=Dog()
c=Cat()
AnimalSound(c)
AnimalSound(d)    


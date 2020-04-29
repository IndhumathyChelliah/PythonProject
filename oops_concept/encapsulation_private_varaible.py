
class Car:
    def __init__(self):
        self.__speed=100
        self.__name="karthicar"
    def drive(self):
        print ("driving")
        print (self.__speed)
    def setspeed(self,speed):
        self.__speed=speed
        print (self.__speed)
c=Car()
c.drive()
c.setspeed(50)



        
        
#introduction to oOOPS

# OOP (Object-Oriented Programming)

# EXAMPLE: car - name, color, speed
# 1) Create a Design for CAR - Class
# 2) To create a Real Product - Object

# Create a class + like a design / blueprint
# Create an object + like a real thing made from that design

#Lets create a class for Car
class Car:
    name="Mahindra Thar"
    price=200000
    color="Black"

#Create A Object For The Class Car
c1=Car() 
print(c1.name)
print(c1.price)
print(c1.color)   
 

c1 -> {name: "Mahindra Thar", price: 200000, color: "Black"} #Object c1 it creates like a real thing from the design of class Car


# Use the "Self" Parameter : Self is A Paramter which is USed to Conncect the Attributes And the Methods defines Inside The Class Connect with Objects
class car:

    def display(self):
        print(f"car Name is{self.name} and the mode is{self.model} Which Is Recent Year and The Proce")

car1=car()
car1.name="BMW"
car1.model=2025
car1.display()


#Use the Constructor "__init__" 
#Constructor : Its is a Special Method "__init__" used to Initialize The Object Attributes When A Class Object is Being Created.It Allows You to SetUp Initialize Values For A Object is Created 
class dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age


    def doggy(self):
        print(f"The Dog is {self.name} and the breed is {self.breed} and the age is {self.age}")  


d1=dog("Tommy","Labrodor",4)
d2=dog("Rex","german",5)
print(d1.doggy())
print(d2.doggy())          

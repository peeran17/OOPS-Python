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

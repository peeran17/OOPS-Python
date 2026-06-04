Inheritance(1st Principle of OOPs):

Definition:
Inheritance is an Object-Oriented Programming (OOP) concept that allows one class to acquire the properties and methods of another class, enabling code reusability and hierarchical relationships between classes.

There are 4 types:
1. Single Inheritance : A child class inherits from only one parent class.
#Ex: #Inheritance : 
class father:
    def gardening(self):
        print("i like Gardening")

class son(father):
    def playing(self):
        print("i love Playing Cricket")        
c1=father()
c2=son()
c1.gardening()
c2.playing()  
c2.gardening()  
c1.playing()     #Error Becuase Father Canot Inherit the Properties From Child 

2. Multilevel Inheritance :
Definition:
A class inherits from a parent class, and another class inherits from that child class, forming a chain.
#Inheritance :
class grandfather:
    def farming(self):
        print("i like Farming") 
class father(grandfather):
    def gardening(self):
        print("i like Gardening")

class son(father):
    def playing(self):
        print("i love Playing Cricket")        

c1=father()
c2=son()
c3=grandfather()
c1.gardening()
c1.farming()
c2.playing() 
c2.gardening 
c2.gardening() 
c3.farming() 




3. Multiple Inheritance: A child class inherits properties and methods from more than one parent class.(Mother,father properties can inherit by Son)
#Inheritance :
class father:
    def farming(self):
        print("i like Farming") 
class mother:
    def gardening(self):
        print("i like Gardening")

class son(father,mother):
    def playing(self):
        print("i love Playing Cricket")        


c1=son()
c1.playing()
c1.gardening()
c1.farming()    


4. Hierarchical Inheritance: Multiple child classes inherit from the same parent class.

class father:
  def Cooking(self):
    print("I will Cook")

class son1(father):
  def playing(self):
    print("I Love Play Football")

class son2(father):
  def singing(self):
    print("I always Sings Song")


p1=son1()
p2=son2()
p1.playing()
p1.cooking()
p2.singing()
p2.cooking()

# Examples 

class vehicle:
    def start(self):
        print("Vehicle is Started")

    def stop(self):
        print("Vehicle has Stopped")

class car(vehicle):
    pass
c=car()
c.start()
c.stop()


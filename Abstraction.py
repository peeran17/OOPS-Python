Abstraction : Abstraction is the process of hiding implementation details and showing only the essential functionality to the user.

Key Idea
WHAT to do  → Visible
HOW to do it → Hidden

The user knows what a method does, but does not need to know how it works internally.
Why Use Abstraction?
-> Reduces complexity
-> Improves code security
-> Makes programs easier to use
-> Focuses on essential features

How Abstraction is Achieved in Python?
Using:
from abc import ABC, abstractmethod
ABC → Abstract Base Class
@abstractmethod → Declares an abstract method


Example Structure:

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")



Important Points:

-> An abstract class cannot be instantiated (object cannot be created directly).
-> Abstract methods must be implemented in child classes.
-> pass is used as a placeholder in abstract methods.
-> The parent class defines the method, and the child class provides the implementation.
  
Real-Life Example:
Mobile Phone
You know:

Call button
Message button

You do not know:

Signal processing
Network communication
Internal hardware operations

The internal working is hidden, and only the required functionality is shown.

Interview Answer:

Abstraction is an OOP principle that hides implementation details and exposes only the necessary functionality. It helps reduce complexity and improves code maintainability.


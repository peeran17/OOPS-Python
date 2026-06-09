# Polymorphism in Python

## Definition

**Polymorphism is an Object-Oriented Programming (OOP) concept in which the same method can have different behaviors depending on the object that calls it.**

## Interview Definition

**Polymorphism allows one interface or method to have multiple implementations, enabling different objects to respond differently to the same method call.**

---

## Key Idea

> **One Method, Many Behaviors**

or

> **Same Name, Different Work**

---

## Real-Life Example

### Payment System

An e-commerce application may support multiple payment methods:

* Credit Card
* UPI
* PayPal

All payment methods use the same method:

```python
pay()
```

However, each payment method processes the payment differently.

This is called **Polymorphism**.

---

## Python Example

```python
class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")

class UPI:
    def pay(self):
        print("Payment made using UPI")

class PayPal:
    def pay(self):
        print("Payment made using PayPal")

payments = [CreditCard(), UPI(), PayPal()]

for payment in payments:
    payment.pay()
```

### Output

```text
Payment made using Credit Card
Payment made using UPI
Payment made using PayPal
```

---

## Explanation

* All classes have the same method name: `pay()`
* Each class provides its own implementation.
* The behavior changes depending on the object.

Therefore, the same method performs different actions.

---

## Advantages

* Code Reusability
* Flexibility
* Easy Maintenance
* Better Scalability

---

## One-Line Viva Answer

**Polymorphism means one method having multiple forms or behaviors.**

---

## Memory Trick

> **Polymorphism = One Method, Many Behaviors**

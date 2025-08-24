# Object-Oriented Programming Assignment (Python)

## Overview
This project demonstrates the fundamentals of Object-Oriented Programming (OOP) in Python.  
It contains two main activities:

1. **Assignment 1: Design Your Own Class 🏗️**  
   - Created a `Smartphone` class with attributes and methods.  
   - Added a `GamingPhone` subclass to demonstrate inheritance and encapsulation.  
   - Showcased how constructors (`__init__`) initialize objects with unique values.  

2. **Activity 2: Polymorphism Challenge 🎭**  
   - Implemented a `Vehicle` base class with a `move()` method.  
   - Subclasses (`Car`, `Plane`, `Boat`) override the `move()` method differently.  
   - Demonstrates polymorphism by calling the same method across different objects.

---

## Features
- **Classes & Objects** → Encapsulating attributes and methods.  
- **Constructors** → Initializing each object with unique values.  
- **Inheritance** → Subclasses extending parent classes.  
- **Polymorphism** → Same method name, different implementations.  

---

## Example Usage

### Smartphone Example
```python
phone1 = Smartphone("Samsung", "Galaxy S24", 20)
phone1.call("0501234567")
phone1.battery_status()
phone2 = Smartphone("Apple", "iPhone 14", 15)
phone2.call("0509876543")
phone2.battery_status()
```

### GamingPhone Example
```python
phone2 = GamingPhone("Asus", "ROG Phone 7", 15, "liquid cooling")
phone2.play_game("PUBG Mobile")
```

### Vehicle Example
```python
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
```

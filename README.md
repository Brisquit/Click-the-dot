# Click-the-dot
A game made using OOP on python, where you need to click the dot.
The code Implements all 4 pillars of Object-Oriented Programming.

# OOP-Pillars
Polymorphism is used to differentiate what kind of randomise.pos is used whenever self.circle is called, which is decided by which self.type is called making for different results each time.

![image](https://github.com/user-attachments/assets/2c972faa-a186-4145-becc-2cdf69881906)

Abstraction is used to in the Start class, which only exposes the necessary methods. 
![image](https://github.com/user-attachments/assets/a593d2f3-2231-4ab5-84f8-04322bd9986b)

Inheritance is used so other classes could inherit draw() and collision() from class Start.
![image](https://github.com/user-attachments/assets/e5a7f7e7-ffe1-47db-bc0a-57cee597ab7a)

Encapsulation is used to encapsulate the data inside the Scores class, and to modify the score in the class instead of changing it from outside.

![image](https://github.com/user-attachments/assets/6a412fd6-43cc-430b-9a0c-33e79eae38f8)

# Design-Pattern
The design pattern implemented in the code the most is Factory, which allows the Game class to initiate a different circle object based on which self.type is chosen, allowing for runtime flexibility.
The Factory design pattern was chosen for it's easy expansion if I ever want to add more types, since I can just make it type == 3 and just add another child class to the Start class.

# Compostition
The code uses Composition in the Game class to give meaning to the other classes, if Game didn't exist, the other classes would lose their meaning.

![image](https://github.com/user-attachments/assets/f1b49200-a52f-4bd1-ab85-c2c3afb6f277)

# How-To-Play
To play the game, you need to double click the .exe file

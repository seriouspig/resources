numbers = [1,2,3]

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(1,2)
point1.draw()
point1.move()

point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point(6,10)
point2.x = 1
print(point2.x)

# CONSTRUCTOR 

point = Point(20, 40)

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self,words):
        print(f'{self.name} said: {words}')

piotr = Person("Piotr")

piotr.talk("What is happening?")

# INHERITANCE 

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    def miau(self):
        print("Miau!!!")

    
dog = Dog()
cat = Cat()

dog.walk()
cat.walk()
cat.miau()

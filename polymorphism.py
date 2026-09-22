class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

class Cat(Animal):

    def sound(self):
        print("Cat Meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

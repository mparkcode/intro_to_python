
class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"I am {self.name}, and I am {self.age} years old"
    
    def speak(self):
        return f"I have nothing to say"

class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)  # Pet('Garam', 12)
        self.colour = colour

    def show_info(self):
        return f"I am {self.name}, and I am {self.age} years old, and I am {self.colour}"
    
    def speak(self):
        return "Meow"
    
class Dog(Pet):
    def speak(self):
        return "Woof"
    
class Fish(Pet):
    pass
    
my_cat = Cat('Garam', 12, 'Brown')
print(my_cat.show_info())

my_dog = Dog('Rover', 8)
print(my_dog.show_info())

my_fish = Fish('Bubbles', 5)
print(my_fish.show_info())
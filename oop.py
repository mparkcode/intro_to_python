# Everything is an object

class Car:

    def __init__(self, make, model, ammount):
        self.ammount = ammount
        self.make = make
        self.model = model

    def drive(self):
        print('You are driving the car')

    def park(self):
        print('You park the car')
    
    def fill_tank(self):
        print(f'You fill the car with ${self.ammount} worth of fuel')

    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def set_make(self, make):
        self.make = make

my_car = Car("Honda", "Civic", 15)
print(my_car.get_make())
my_car.set_make("Volvo")
print(my_car.get_make())

# print(my_car.get_make())
# print(my_car.get_model())

# your_car = Car("Toyota", "Camry", 50)
# print(your_car.get_make())
# print(your_car.get_model())
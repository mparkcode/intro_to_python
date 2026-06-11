import os
os.system('clear')

class Bird:

    #Constructor
    def __init__(self, kind, call):
        print("In the bird constructor")

        #Instance Attributes
        self.kind = kind
        self.call = call

    #Instance Methods
    def describe(self):
        return f"{self.kind} goes {self.call}"
    
    def intro(self):
        return f"Please to meet you, I am a {self.kind}"
    
class BigBird(Bird):

    #Constructor 
    def __init__(self, kind, call, wingspan):
        print("In the big bird constructor")
        super().__init__(kind, call)
        self.wingspan = wingspan

    #Instance Methods
    def describe(self):
        return f"{self.kind} goes {self.call}, and has a wingspan of {self.wingspan} meters"
    
class ReallyBigBird(BigBird):

    #constructor
    def __init__(self, kind, call, wingspan, age):
        print("In the really big bird constructor")
        super().__init__(kind, call, wingspan)
        self.age = age

    #Instance Methods
    def describe(self):

        return (f"{self.kind} goes {self.call}, and has a wingspan of " 
                f"{self.wingspan} meters, and is {self.age} years old")

# sparrow = Bird("Sparrow", "Tweet")
# eagle = BigBird("Eagle", "Caw", 65)
vulture = ReallyBigBird("Vulture", "Screech", 100, 30)
# print(sparrow.describe())
# print(eagle.describe())
print(vulture.intro())
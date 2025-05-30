from abc import ABC, abstractmethod
 
class Factory(ABC): # Factory is an abstract class that defines the create_product method
   
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class AnimalFactory(Factory): # AnimalFactory is a concrete class that implements the create_product method
    def __init__(self):
        pass
 
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()
 
        return animal
 
class DogFactory(Factory): # DogFactory is a concrete class that implements the create_product method
   
    def create_product(self, kind=None):
        return Dog() # fixed the issue by returning the Dog object instead of passing it as an argument
 
class CatFactory(Factory): # CatFactory is a concrete class that implements the create_product method
   
    def create_product(self, kind=None):
        return Cat() # fixed the issue by returning the Cat object instead of passing it as an argument
 
class Animals(ABC): # Animals is an abstract class that defines the run method
 
    @abstractmethod
    def run(self):
        pass
 
class Dog(Animals): # Dog is a concrete class that implements the run method
 
    def run(self):
        print(f"I'm a Dog, I can run!!")
 
 
class Cat(Animals): # Cat is a concrete class that implements the run method
    def __init__(self):
        pass
 
    def run(self):
        print(f"I'm a Cat, I can run!!")
 
 
 
 
 
# client
factory = DogFactory()
#dog = Dog()
dog = factory.create_product()
 
dog.run()
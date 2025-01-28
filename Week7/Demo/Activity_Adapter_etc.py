# ============================================================================
#  Activity : analyse the following modules with short description ===========
# ============================================================================

# Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True

# Factory Pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

# Usage
animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Output: Woof!

# Observer Pattern
class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Usage
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Event occurred!")  
# Output:
# Observer 1 received: Event occurred!
# Observer 2 received: Event occurred!

# Decorator Pattern
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

# Usage
say_hello()
# Output:
# Before function execution
# Hello!
# After function execution

# Strategy Pattern
class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Strategy A executed"

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Strategy B executed"

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.execute()

# Usage
context = Context(ConcreteStrategyA())
print(context.execute_strategy())  # Output: Strategy A executed

context.strategy = ConcreteStrategyB()
print(context.execute_strategy())  # Output: Strategy B executed

# Adapter Pattern
class OldSystem:
    def old_method(self):
        return "Old system method"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return self.old_system.old_method()

# Usage
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.new_method())  # Output: Old system method

# Builder Pattern
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        return "Product parts: " + ", ".join(self.parts)

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_product(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def get_product(self):
        return self.product

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

# Usage
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_product()
print(product.show())  # Output: Product parts: Part A, Part B

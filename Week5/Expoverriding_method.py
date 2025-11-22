# Grandparent class
class GrandParent:
    def greeting(self):
        return "Hello from GrandParent!"

# Parent class inherits from GrandParent
class Parent(GrandParent):
    def greeting(self):
        return "Hello from Parent!"

# Child class inherits from Parent
class Child(Parent):
    def greeting(self):
        return "Hello from Child!"

if __name__ == "__main__":
    # Demonstration
    gp = GrandParent()
    p = Parent()
    c = Child()

    print(gp.greeting())   # Uses GrandParent's method
    print(p.greeting())    # Overrides to Parent's method
    print(c.greeting())    # Overrides again to Child's method

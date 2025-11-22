# class Circle:
#     def draw(self):
#         return "Drawing a Circle"

# class Square:
#     def draw(self):
#         return "Drawing a Square"

# class ShapeFactory:
#     def create_shape(self, shape_type):
#         if shape_type == "circle":
#             return Circle()
#         if shape_type == "square":
#             return Square()
#         else:
#             return None


# factory = ShapeFactory()
# shape = factory.create_shape("triangle")   
# print(shape.draw())  


#=============================
from abc import ABC, abstractmethod

# 1) Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        """Render the shape and return a description."""
        pass


# 2) Concrete Products
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"


class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"


# 3) Factory
class ShapeFactory:
    _registry = {
        "circle": Circle,
        "square": Square,
    }

    @classmethod
    def register(cls, name: str, shape_cls: type[Shape]) -> None:
        """Optionally register new shapes without modifying factory code."""
        if not issubclass(shape_cls, Shape):
            raise TypeError("Registered class must inherit from Shape")
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create(cls, shape_type: str) -> Shape:
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()


# 4) Client code (examples)
if __name__ == "__main__":
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())   # -> "Drawing a Circle"

    square = factory.create("square")
    print(square.draw())   # -> "Drawing a Square"

    # This will raise a clear error instead of failing at runtime with NoneType:
    # triangle = factory.create("triangle")

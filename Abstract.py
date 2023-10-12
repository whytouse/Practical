from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
    
class square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4

#object of class  
Circle = Circle(int(input("Enter raduius of Circle:")))
square = square(int(input("Enter side of square:")))

#Expression
print(f"Area Of Circle is ={Circle.area()}")
print(f"Perimeter Of Circle is ={Circle.perimeter()}")
print(f"Area Of Square is ={square.area()}")
print(f"Perimeter Of Square is ={square.perimeter()}")

#Define circle class to create a circle with radius r using the constructor, 
#define an area() method of the class which calculates the area of the circle.
#Define Perimeter() method of the class which allows you to calculate the premire of the circle.

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return  (22/7)*self.radius**2
    
    def Perimeter(self):
        return 2*(22/7)*self.radius
  
c1 = Circle(21)

print(c1.area())
print(c1.Perimeter())  

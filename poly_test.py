class Point:
    def __init__(self, x, y):
        self.x  = x
        self.y = y 

    def __add__ (self, other):
        x  = self.x + other.x 
        y = self.y + other.y 
        return x, y 

p1 = Point(2, 3)
p2 = Point(3, 4) 
print(p1 + p2) 
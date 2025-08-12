class Point:
    """ Point class for representing and manipulating x, y coordinates."""
 
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def print(self):
        print((self.x, self.y))   

    def translation(self, dx: float, dy: float):
        """Move a point by a certain amount along the x and y axes."""
        self.x = self.x + dx
        self.y = self.y + dy


def distance(p1: Point, p2: Point) -> float:
    """Calculate distance between two points"""
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

def midpoint(p1: Point, p2: Point) -> Point:
    return Point((p1.x + p2.x)/2,(p1.y + p2.y)/2)


point1 = Point()
point2 = Point(2, 3)

print(point1)
print(point2)
point1.print()

midpoint = midpoint(point1, point2)
midpoint.print()
print("Distance between p1 and p2: {}",distance(point1,point2))


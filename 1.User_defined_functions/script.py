class Point():
    # Definning a method.
    def getX(self):
        return self.x


# Creating instances
point1 = Point()
point2 = Point()

# Creating instance variables.
point1.x = 5
point2.x = 10

# Accessing instance variables
print(point1.x)
print(point2.x)

# Accessing methods
print(point1.getX())
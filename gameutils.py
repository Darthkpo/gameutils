from math import sqrt, atan2, degrees, pi

RED = (255,0,0)
DARK_GRAY = (40,40,40)
LIGHT_GRAY = (200,200,200)
LIGHT_ORANGE = (255,200,80)
BLACK = (0,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0,40,0)
BLUE = (0,0,255)

class Vector2:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector2: (%f,%f)" % (self.x,self.y)

    def __add__(self,other):
        if type(other) is Vector2 or isinstance(other, self.__class__):
            return Vector2(self.x + other.x, self.y + other.y)
        if type(other) is float:
            return Vector2(self.x + other, self.y + other)
        if type(other) is int:
            return Vector2(self.x + other, self.y + other)

    def __sub__(self,other):
        if type(other) is Vector2 or isinstance(other, self.__class__):
            return Vector2(self.x - other.x, self.y - other.y)
        if type(other) is float:
            return Vector2(self.x - other, self.y - other)
        if type(other) is int:
            return Vector2(self.x - other, self.y - other)

    def __mul__(self,other):
        if type(other) is Vector2 or isinstance(other, self.__class__):
            return Vector2(self.x * other.x, self.y * other.y)
        if type(other) is float:
            return Vector2(self.x * other, self.y * other)
        if type(other) is int:
            return Vector2(self.x * other, self.y * other)

    def __div__(self,other):
        if type(other) is Vector2 or isinstance(other, self.__class__):
            return Vector2(self.x / other.x, self.y / other.y)
        if type(other) is float:
            return Vector2(self.x / other, self.y / other)
        if type(other) is int:
            return Vector2(self.x / other, self.y / other)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def lenght(self):
        return sqrt((self.x * self.x) + (self.y * self.y))

    def normalize(self):
        L = self.lenght()
        return Vector2(self.x / L if L != 0 else 0, self.y / L if L != 0 else 0) 

def get_angle(origin, destination):
    # Returns angle in radians from origin to destination.
    # This is the angle that you would get if the points were
    # on a cartesian grid. Arguments of (0,0), (1, -1)
    # return .25pi(45 deg) rather than 1.75pi(315 deg).
    
    x_dist = destination.x - origin.x
    y_dist = destination.y - origin.y
    return degrees(atan2(-y_dist, x_dist) % (2 * pi))

def snap_to_grid(point,grid_size):
    return Vector2(point.x / grid_size,point.y / grid_size)

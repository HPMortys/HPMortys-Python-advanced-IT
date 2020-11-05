class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def setCord_x(self):
        self.x = input('Enter new x: ')

    def setCord_y(self):
        self.x = input('Enter new y: ')

    def setCord_z(self):
        self.z = input('Enter new z: ')

    def getCord_x(self, ):
        return self.x

    def getCord_y(self, ):
        return self.y

    def getCord_z(self):
        return self.z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z

point_0 = Point(1, 2, 3)
point_1 = Point(1, 2, 3)

print(point_0 * point_1)

class Point3D:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def info(self):
        print(f'x = {self.x},y = {self.y},z = {self.z}')

    def distance(self):
        dxy = self.y - self.x
        dzy = self.z - self.y
        print(f'Расстояние между xy: {dxy},Расстояние между zy: {dzy}')

    def double(self):
        return 2*self.x,2*self.y,2*self.z

a = Point3D(50,22,-10)
b = Point3D(8,435,7)
c = Point3D(-123,-4444,123)
a.info()
b.info()
c.info()
a.distance()
a.z = 12343241231234324324
a.info()
print(a.double())

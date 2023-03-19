class Class1:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        print("x=", self.x)


class Class3:
    def __init__(self, z):
        self.z = z

    def get_z(self):
        print("z=", self.z)

class Class2(Class1, Class3):
    def __init__(self, x, y, z):
        super().__init__(x)
        Class3.__init__(self, z)
        self.y = y
    def get_self(self):

class Class4:7891230+



c1 = Class1(5)
c2 = Class2(15)

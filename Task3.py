class Tri:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Stri(self):
        print(f'S = {self.a*self.b/2}')
    def Ptri(self):
        c = (self.a**2 + self.b**2)**0.5
        print(f'P = {self.a + self.b + c}')

Tri = Tri(3,5)
Tri.Ptri()
Tri.Stri()
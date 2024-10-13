from math import *
class Circle:
    def __init__(self,r):
        self.r=r
    def show(self):
        print('圆的半径为：',self.r)
    def Area(self):
        return pi*self.r*self.r
class CZ(Circle):
    def __init__(self,r,h):
        super(CZ,self).__init__(r)
        self.h=h
    def changer(self,r):
        self.r=r
    def changeh(self,h):
        self.h=h
    def show(self):
        print("圆柱的半径和高分别为",self.r,self.h)
    def V(self):
        return self.r*self.r*self.h*pi
cz=CZ(1,2)
cz.show()
print(cz.V())
cz.changeh(4)
cz.show()
cz.changer(3)
cz.show()


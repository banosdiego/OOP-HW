#test
class Line:
    def __init__(self,coordinate1,coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        x1,y1 = coordinate1
        x2,y2 = coordinate2
        return ((((x2 - x1)**2) + ((y2 - y1)**2))**(1/2))

    def slope():
        pass
coordinate1=(3,2)
coordinate2=(8,10)

l = Line(coordinate1,coordinate2)
a = l.distance()
print(a)
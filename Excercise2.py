class Cylinder:
    # cylinder's volume is π r² h, and its surface area is 2π r h + 2π r²
    
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.radius = radius
        self.height = height

    def volume(self):
        h = self.height
        r = self.radius
        pi = self.pi
        return h*pi*r**2

    def surface_area(self):
        h = self.height
        r = self.radius
        pi = self.pi
        return ((2*pi)*(r*h))+((2*pi)*(r**2))
    

cilindro = Cylinder(2,3)
surface = cilindro.surface_area()
volume = cilindro.volume()
print (volume)
print (surface)
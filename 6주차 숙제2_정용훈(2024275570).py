import matplotlib.pyplot as plt

class Circle(object):
    def __init__(self, radius, color='blue'):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle = Circle(0, 'red')
RedCircle.radius
RedCircle.add_radius(2)
RedCircle.radius
RedCircle.add_radius(2)
RedCircle.radius
RedCircle.add_radius(2)
print(RedCircle.radius)

RedCircle = Circle(1,'red')
RedCircle.radius
print(RedCircle.radius)

dir(RedCircle)

RedCircle.radius
print(RedCircle.radius)

RedCircle.color
print(RedCircle.color)

RedCircle.radius = 12
RedCircle.radius
print(RedCircle.radius)

RedCircle.radius = 20
RedCircle.drawCircle()

print('Radius of object:', RedCircle.radius)
RedCircle.add_radius(2)
RedCircle.drawCircle()
RedCircle.radius

RedCircle.radius
print(RedCircle.radius)

RedCircle.add_radius(2)
print(RedCircle.add_radius)

RedCircle.drawCircle()

BlueCircle = Circle(radius=100)
BlueCircle.radius
BlueCircle.color

BlueCircle.drawCircle()

class Rectangle(object):

    def __init__(self, width = 2, height = 3, color = 'r'):
        self.height = height
        self.width = width
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

SkinnyBlueRectangle = Rectangle(2, 10, 'blue')
SkinnyBlueRectangle.height
print(SkinnyBlueRectangle.height)

SkinnyBlueRectangle.width
print(SkinnyBlueRectangle.width)

SkinnyBlueRectangle.color
print(SkinnyBlueRectangle.color)

SkinnyBlueRectangle.drawRectangle()

FatYellowRectangle = Rectangle(20, 5, 'yellow')

FatYellowRectangle.height
print(FatYellowRectangle.height)

FatYellowRectangle.width
print(FatYellowRectangle.width)

FatYellowRectangle.color
print(FatYellowRectangle.color)

FatYellowRectangle.drawRectangle()
# Planet Class
from turtle import *
class Planet:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y
        canvas = Screen()
        canvas.setup(800, 800)
        self.turtle = Turtle()

    def circumference(self):
        return 2*3.1415*self.radius

    def scaleSize(self, scale):
        self.radius = self.radius*scale

    def draw(self, colour):
        self.turtle.goto(self.x, self.y)
        self.turtle.color(colour)
        self.turtle.dot(self.radius)



#====instance of the class===
planet1 = Planet(-200, -100, 200)
planet1.draw('red')
print('Circumference *check the maths!* is:', planet1.circumference())
planet1.scaleSize(0.5)
planet1.draw('yellow')
planet2 = Planet(300, 200, 100)
planet2.draw('black')

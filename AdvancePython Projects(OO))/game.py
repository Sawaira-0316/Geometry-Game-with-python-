from random import randint

import turtle
class point:
     def __int__(self,x,y):
         self.x=x
         self.y=y
     def falls_in_rectangular(self,rectangular):
         if rectangular.point1.x < self.x < rectangular.point2.x \
                and rectangular.point1.y < self.y <rectangular.point2.y:
             return True
         else:
             return False
class Rectangular:
    def __int__(self,point1,point2):
        self.point1=point1
        self.point2=point2
    def area(self):
        return (self.point2.x - self.point1.x)* \
            (self.point2.y - self.point1.y)

class GuiRectangular(Rectangular):
    def drew(self,canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)

        canvas.forward(100)
        canvas.left(90)
        canvas.forward(200)
        canvas.left(90)
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(200)

        canvas.done()


rectangular=GuiRectangular(point(randint(0, 9), randint(0, 9)),
                          point(randint(10, 19), randint(10, 19)))

myturtle=turtle.Turtle()
GuiRectangular.drew(canvas=turtle)

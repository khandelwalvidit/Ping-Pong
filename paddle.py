from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,cordinates) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.turtlesize(5,1,1)
        self.goto(cordinates)
        self.xcordinate = self.xcor()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x = self.xcordinate,y=new_y)

    def down(self):
        new_y = self.ycor() - 20      
        self.goto(x=self.xcordinate,y=new_y)

# Isaac Hartzell
# 7-1-2019
# This program demonstrates a circle, square, and triangle being drawn
# on the screen with different backgrounds, titles, and pen colors using the turtle library.
# ------------------------------------------------------------------------------------------
# Justification for factory and strategy design patterns: Here is my justification,
# I'm going to be making different shapes that all have the same methods, but they do different things.
# This seems like a perfect use of the strategy design pattern as the design makes it so there's an interface
# which all the shape classes inherit, and then a Context class is made where the functions correctly associated
# with the specific shapes are performed. The factory design pattern comes into play because I'm going to be making
# instances of different shapes, so it would be great to have a factory that creates the instances of the shapes
# and then I can throw that into my StrategyContext class to execute the appropriate functions for the appropriate
# shapes.
import turtle
import time


# I'm making this interface althrough in python there aren't really true interfaces, but it's to be treated
# as such. I'm making this because I'm going to have specific shapes that all implement the methods of this
# interface, but for each shape they perform these methods differently doing slightly different things.
# For example, a triangle and a square both can draw, but a triangle draws a triangle, a square draws a square.
class Shape(object):

    def draw(self):
        raise NotImplementedError

    def background_color(self):
        raise NotImplementedError

    def pen_color(self):
        raise NotImplementedError

    def change_title(self):
        raise NotImplementedError


# I'm making this class, and inheriting from Shape because a circle is going to have all the methods that shape
# has, but it's going to implement them in a specific way to shape.
class Circle(Shape):
    # Creating the pen and screen for the turtle canvas as well as the size of the pen and its speed.
    def __init__(self, pen, screen):
        self.pen = pen
        self.screen = screen
        self.pen.pensize(10)
        self.pen.speed(1)

    def draw(self):
        # 100 is the radius of the circle.
        self.pen.circle(100)

    def background_color(self):
        self.screen.bgcolor("green")

    def pen_color(self):
        self.pen.color("yellow")

    def change_title(self):
        self.screen.title("Circle Canvas")


class Square(Shape):
    def __init__(self, pen, screen):
        self.pen = pen
        self.screen = screen
        self.pen.pensize(10)
        self.pen.speed(1)

    # The pen moves forward 100 spaces forward, then turns left 90 degrees and repeats 4 times making a square.
    def draw(self):
        for i in range(4):
            self.pen.forward(100)
            self.pen.left(90)

    def background_color(self):
        self.screen.bgcolor("red")

    def pen_color(self):
        self.pen.color("pink")

    def change_title(self):
        self.screen.title("Square Canvas")


class Triangle(Shape):
    def __init__(self, pen, screen):
        self.pen = pen
        self.screen = screen
        self.pen.pensize(10)
        self.pen.speed(1)

    def draw(self):
        self.pen.forward(100)
        self.pen.left(90)
        self.pen.forward(100)
        self.pen.left(135)
        self.pen.forward(142)

    def background_color(self):
        self.screen.bgcolor("grey")

    def pen_color(self):
        self.pen.color("white")

    def change_title(self):
        self.screen.title("Triangle Canvas")


# I'm making this class because I need a class for establishing different strategies for the different shapes.
class StrategyContext(object):
    # Each shape will be different passed into this constructor.
    def __init__(self, shape):
        self.shape = shape

    # This function will execute the different methods specific to the specific shape passed into the constructor,
    # hence the context.
    def execute_strategy(self, a_string):
        a_string = a_string.lower()
        if a_string == "change title":
            return self.shape.change_title()
        elif a_string == "background color":
            return self.shape.background_color()
        elif a_string == "pen color":
            return self.shape.pen_color()
        elif a_string == "draw":
            return self.shape.draw()
        else:
            print("There is no function for this shape.")


# Making this class so I have a simple way of creating my specific shapes.
class ShapeFactory(object):
    # static because I don't need to make an instance.
    @staticmethod
    def get_shape(type):
        if type == "circle":
            pen = turtle.Turtle()
            screen = turtle.Screen()
            return Circle(pen, screen)
        elif type == "square":
            pen = turtle.Turtle()
            screen = turtle.Screen()
            return Square(pen, screen)
        elif type == "triangle":
            pen = turtle.Turtle()
            screen = turtle.Screen()
            return Triangle(pen, screen)
        else:
            print("This shape doesn't exist.")


def main():
    print("I will be showing a series of test cases. The three cases are for drawing a circle, a square, "
          "and a triangle.\nFor each shape they have the following: a different title, a different pen color,"
          "a different background color, and lastly a different shape drawn.")
    time.sleep(15)  # Suspends the output screen so the user can read about the test cases before they're shown.
    # For the test cases I'm doing the same thing. I'm making a factory instance, then I use
    # the factory instance so I can create the shape I want. I then pass this shape to the StrategyContext class
    # so I show all the associated functions in work for that specific shape. I then
    # show for each shape the title of the canvas changing, the background color changing, the pen color changing, and
    # lastly drawing the shape. In between these function demonstrations I have the canvas freeze for a couple seconds
    # before showing the next function in work. I then clear the turtle screen canvas for the next shape's
    # demonstration.
    circle = ShapeFactory.get_shape('circle')
    strat_for_circle = StrategyContext(circle)

    strat_for_circle.execute_strategy("change title")
    time.sleep(2)
    strat_for_circle.execute_strategy("background color")
    time.sleep(2)
    strat_for_circle.execute_strategy("pen color")
    time.sleep(2)
    strat_for_circle.execute_strategy("draw")
    time.sleep(2)
    turtle.clearscreen()

    square = ShapeFactory.get_shape('square')
    strat_for_square = StrategyContext(square)

    strat_for_square.execute_strategy("change title")
    time.sleep(2)
    strat_for_square.execute_strategy("background color")
    time.sleep(2)
    strat_for_square.execute_strategy("pen color")
    time.sleep(2)
    strat_for_square.execute_strategy("draw")
    time.sleep(2)
    turtle.clearscreen()

    triangle = ShapeFactory.get_shape('triangle')
    strat_for_triangle = StrategyContext(triangle)

    strat_for_triangle.execute_strategy("change title")
    time.sleep(2)
    strat_for_triangle.execute_strategy("background color")
    time.sleep(2)
    strat_for_triangle.execute_strategy("pen color")
    time.sleep(2)
    strat_for_triangle.execute_strategy("draw")
    time.sleep(2)
    turtle.clearscreen()


if __name__ == '__main__':
    main()
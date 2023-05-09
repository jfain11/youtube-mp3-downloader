from graphics import *

class Button:
    """
    makes a usable button for the graphics class
    """

    def __init__(self, x: int, y: int, height: int, width: int):
        """
        initializes the button
        :param x: x coordinate of the center point
        :param y: x coordinate of the center point
        :param height: the height of the button
        :param width: the width of the button
        """
        self.p1 = Point(x - width / 2, y + height / 2)
        self.p2 = Point(x + width / 2, y - height / 2)
        self.button = Rectangle(self.p1, self.p2)

    def draw(self, win: GraphWin):
        """
        draws the button in the window
        :param win: the graphics win
        :return: None
        """
        self.button.draw(win)

    def isClicked(self, click: Point) -> bool:
        """
        checks if the button is clicked
        :param click: the point of the mouse click
        :return: True if the button was clicked and False if not
        """
        if self.p1.getX() < click.getX() < self.p2.getX() and self.p1.getY() > click.getY() > self.p2.getY():
            return True
        else:
            return False

    def setFill(self, color: str):
        """
        changes the color of the button
        :param color: enter a color in the form of a string
        :return: None
        """
        self.button.setFill(color)

    def setWidth(self, width: int):
        """
        sets the width of the button's border
        :param width: the width of the border
        :return: None
        """
        self.button.setWidth(width)

    def undraw(self):
        """
        undraws the button from the window
        :return: None
        """
        self.button.undraw()


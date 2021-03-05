class Square:
    def __init__(self, side):
        self.height = side
        self.__width = side
    @property
    def height(self):
        return self.__height, self.__width
    @height.setter
    def height(self, new_side):
        if new_side >= 0:
            self.__height = new_side
            self.__width = new_side
        else:
            raise Exception('Value needs to be 0 or larger.')

sq1 = Square(2)
mh = sq1.height()
print(mh)
sq1.height(5)
mh = sq1.height()
print(mh)
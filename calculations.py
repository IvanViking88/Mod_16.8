from figures_base import Rectangle, Square, Circle

rect_1 = Rectangle(4, 6)
rect_2 = Rectangle(12, 8)

square_1 = Square(6)
square_2 = Square(12)

circle_1 = Circle(8)
circle_2 = Circle(15)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_sq())
    elif isinstance(figure, Rectangle):
        print(figure.get_area_rect())
    else:
        print(figure.get_area_circle())





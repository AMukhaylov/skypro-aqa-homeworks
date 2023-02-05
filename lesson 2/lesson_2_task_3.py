
side_square = float(input("Динна одной стороны квадрата = "))

import math

def area_square(side_square): 
    area = side_square*side_square
    print("Значит площадь будет =", area)

area_square(math.ceil(side_square))
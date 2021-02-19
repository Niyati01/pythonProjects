# No of cans required to paint a wall 
 #  area = h * w
 #  no of cans = area / coverage

import math

def paintAreaCalc(wall_height, wall_width, coverage):
    no_of_cans = math.ceil((wall_height * wall_width) / coverage)
    print(f"You will need {no_of_cans} cans")

height = int(input("Enter the height of the wall : "))
width = int(input("Enter the width of the wall: "))

cov = 5

paintAreaCalc(wall_height = height, wall_width= width ,coverage = cov)
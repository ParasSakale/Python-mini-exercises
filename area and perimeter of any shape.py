def area_of_square(side: float):
    return side * side
def perimeter_of_square(side: float):
    return 4 * side


def area_of_rectangle(length:float, breadth: float):
    return length * breadth
def perimeter_of_rectangle(length:float, breadth: float):
    return 2 * (length + breadth)


def area_of_circle(radius:float):
    return 3.14 * (radius ** 2)
def circumference_of_circle(radius:float):
    return 2 * 3.14 * radius


my_str = """
Let's calculate the Area and the Perimeter of the shape of your choice

Please enter the respective Shape
"""
print(my_str)


while True:
    shape_choice = (input("Choose a shape (Square/Rectangle/Circle): "))

    if shape_choice == 'Square':
        print("Here Area and Perimeter of Square will be calculated")
        parameter = float(input("Enter length of side : "))

        area = area_of_square(parameter)
        perimeter = perimeter_of_square(parameter)
        print(f"Area of Square is : {area}")
        print(f"Perimeter of Square is : {perimeter}")

    elif shape_choice == 'Rectangle':
        print("Here Area and Perimeter of Rectangle will be calculated")
        parameter = float(input("Enter length:"))
        parameter_1 = float(input("Enter breadth:"))

        area = area_of_rectangle(parameter, parameter_1)
        perimeter = perimeter_of_rectangle(parameter, parameter_1)
        print(f"Area of Rectangle is : {area}")
        print(f"Perimeter of Rectangle is : {perimeter}")

    else:
        print("Here Area and Circumference of Circle will be calculated")
        parameter = float(input("Enter radius:"))
        area = area_of_circle(parameter)
        perimeter = circumference_of_circle(parameter)

        print(f"Area of circle is : {area}" )
        print(f"Circumference of circle is : {perimeter}")

    calculate_again = str(input("\nCalculate for another shape? (y/n):"))
    if calculate_again != 'y':
        print("Thank you for using the area and perimeter calculator for any shape")
        break






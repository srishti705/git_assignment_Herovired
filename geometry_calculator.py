import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width


if __name__ == "__main__":
    calculator = GeometryCalculator()

    # Circle Area
    radius = 5
    circle_area = calculator.calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} = {circle_area}")

    # Rectangle Area
    length = 10
    width = 6
    rectangle_area = calculator.calculate_rectangle_area(length, width)
    print(f"The area of the rectangle with length {length} and width {width} = {rectangle_area}")

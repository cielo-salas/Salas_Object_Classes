# This program will compute and print the area and perimeter of a circle
import time


class Circle:
    radius = 0

    def __init__(self, radius):
        self.area = 3.14 * (radius ** 2)
        self.perimeter = 2 * radius * 3.14

    def circle_area_and_perimeter(self):
        print("The area of a circle is", self.area, "and the perimeter of the circle is", self.perimeter)


while True:
    user_input = int(input("\nEnter the radius of the circle:"))
    result = Circle(user_input)
    result.circle_area_and_perimeter()

    delay_second = 1
    time.sleep(delay_second)
    # ask the user if it wants to try again
    choices = int(input("\nDo you want to try again?"
                        "\nIf YES press [1]"
                        "\nIf NO press [2]"
                        "\nEnter here:"))
    if choices == 1:
        print("You  choose to try again.")
        continue
    else:
        print("You choose not to try again.")
        break

"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-12 15:42
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-12 15:42
@Title : Calculate Distance
"""
import math


def calculate_distance(first_point, second_point):
    return math.sqrt(first_point * first_point + second_point * second_point)


if __name__ == "__main__":
    try:
        x = int(input("Enter the value of x coordinate: "))
        y = int(input("Enter the value of y coordinate: "))
        euclidean_distance = calculate_distance(x, y)
        print("Euclidean distance = ", euclidean_distance)
    except Exception as e:
        print("Enter valid input", e)

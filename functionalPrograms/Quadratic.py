"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-12 20:42
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-12 20:42
@Title : Quadratic equation
"""
import math


def calculate_root(a, b, c):
    delta = b * b - 4 * a * c

    if delta < 0:
        print("Roots are Imaginary")
    elif delta >0:
        root1 = (-b + math.sqrt(delta / (2 * a)))
        root2 = (-b - math.sqrt(delta / (2 * a)))
    elif delta == 0:
        root1 = (-b / 2 * a)
        root2 = (-b / 2 * a)

    return root1, root2


if __name__ == "__main__":
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        first_root, second_root = calculate_root(a, b, c)
        print(f"First root : {first_root}\nSecond root : {second_root}")
    except Exception as e:
        print("Enter valid input", e)

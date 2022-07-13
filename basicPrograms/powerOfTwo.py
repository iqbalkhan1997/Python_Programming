"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-09 8:30
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-09 8:30
@Title : Power of Two
"""


def power_of_two(num):
    """
    Description:
       It gives the power of two of the numbers till given input number
    Parameter:
        Passing power value of n
    Return:
        Returning power of 2 until n value
    """
    for i in range(number + 1):
        value = 2 ** i
    return value


if __name__ == "__main__":
    number = int(input("Enter the number of time you want to calculate 2 power value: "))
    if (number <= 0) or (number > 31):
        print("Enter a valid Range from 0 to 31")
    else:
        print(power_of_two(number))

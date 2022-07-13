"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-09 8:30
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-09 8:30
@Title : Harmonic Number
"""


def harmonic(num):
    """
      Description:
          Prints the nth Harmonic Number
      Parameter:
          None
      Return:
          Returning nth Harmonic Number
   """
    number = 1.0
    total_value = 1

    for i in range(num - 1):
        total_value += 1 / number + 1
        number = number + 1
    return total_value


if __name__ == "__main__":
    n = int(input("Enter the number to print its harmonic value : "))
    value = harmonic(n)
    print(f"Entered number harmonic value is : {value}")

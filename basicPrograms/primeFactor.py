"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-09 8:30
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-09 8:30
@Title : Prime Factor
"""


def prime_factor(number):
    """
      Description:
          Gives the prime factor of given number
      Parameter:
          Passing number n
      Return:
          Returning prime factor od n value
   """
    factors = []
    i = 2
    while i <= number:
        if number % i == 0:
            factors.append(i)
            number = number / i

        else:
            i += 1

    return factors


if __name__ == "__main__":
    number = int(input("Enter any number: "))
    print(prime_factor(number))

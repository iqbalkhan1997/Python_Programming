"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-09 8:30
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-09 8:30
@Title : Leap Year
"""


def leap_year_check(year_number):
    """
        Description:
            Print the year is a Leap Year or not.
        Parameter:
            Passing int variable as year
        Return:
            Returning true if year is a multiple of 4 and not multiple of 100, OR year is multiple of 400
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


year = int(input("Enter the year :"))
if leap_year_check(year):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

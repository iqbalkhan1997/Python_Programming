"""
    @Author: Ghouri Iqbal Khan
    @Date: 2022-07-12 23:45
    @Last Modified by: Ghouri Iqbal Khan
    @Last Modified time: 2022-07-12 23:45
    @Title : Gambler
"""
import random


class Coupon:
    def generate_coupon(self, lower, upper, number):
        """
            Description:
                Function to Generate Distinct Coupon Number
            Parameter:
                Passing number of  coupon Digit.
            Return:
                returning Distinct Coupon Number.
        """
        coupon_numbers = set([])
        for i in range(number):
            coupon = random.randint(lower, upper)
            print(coupon)
            coupon_numbers.add(coupon)

        return coupon_numbers


if __name__ == "__main__":
    coupon = Coupon()
    lower_range = int(input("Enter the lower range: "))
    upper_range = int(input("Enter the upper range: "))
    number = int(input("Enter number of unique coupon numbers to generate: "))
    list = coupon.generate_coupon(lower_range, upper_range, number)
    print(list)

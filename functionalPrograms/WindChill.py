"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-12 20:42
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-12 20:42
@Title : Prints the wind chill.
"""

import math


def calculate_wind_chill(temp, vel):
    """
        Description:
            Function to calculate Wind Chill
        Parameter:
            take input temperature from user
        Return:
            Returning the Wind Chill Value
    """
    if 3 <= vel <= 120 and temp < 50:
        return 35.74 + (0.6215 * temp) + (0.4275 * temp - 35.75) * (math.pow(vel, 0.16))
    else:
        return "Velocity should be in range 3 - 120 mile/hr \nTemperature should be less than 50 F"


if __name__ == "__main__":
    try:
        temperature = float(input("Enter the value of temperature(in fahrenheit): "))
        velocity = float(input("Enter the value of velocity(in miles per hour): "))
        wind_chill = calculate_wind_chill(temperature, velocity)
        print("Effective temperature is: ", wind_chill)
    except Exception as e:
        print("Enter valid input", e)

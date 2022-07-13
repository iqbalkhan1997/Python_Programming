"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-09 8:30
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-09 8:30
@Title : Flip Coin
"""

import random


def flip_coin(count):
    """
    Description:
            This function takes the no of flips as input and output the percentage of head and tails
    Parameter:
            using random value to generate heads and tails through if condition format
    Return:
            Return the head's percentage of a coin flipped
    """
    head = 0
    tail = 0
    for i in range(count):
        random_num = random.randint(0, 1)
        if random_num == 1:
            head += 1
        tail += 1
    head_percentage = head / count * 100
    return head_percentage


if __name__ == "__main__":
    count = int(input("Enter the number of times you want to flip coin :"))
    head_percentage = round(flip_coin(count), 2)
    tail_percentage = round(100 - head_percentage, 2)
    print(f"Head Percentage is : {head_percentage}%")
    print(f"Tail Percentage is : {tail_percentage}%")

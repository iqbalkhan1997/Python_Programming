"""
    @Author: Ghouri Iqbal Khan
    @Date: 2022-07-12 22:45
    @Last Modified by: Ghouri Iqbal Khan
    @Last Modified time: 2022-07-12 22:45
    @Title : Gambler
"""
import random


class Gamble():

    def gambling(self, stake, goal):
        """
            Description:
                Whether the player play the Gambler game
            Parameter:
                Passing value of stake goal and number of times trial
            Return:
                Return the percentage of win and loss
        """
        win_count = loss_count = game_count = 0
        while stake != 0 and stake != goal:
            game_result = random.random()
            if game_result <= 0.5:
                stake += 1
                win_count += 1
                game_count += 1
            else:
                stake -= 1
                loss_count += 1
                game_count += 1
        win_percentage = win_count / game_count * 100
        loss_percentage = loss_count / game_count * 100
        print("Win percentage is ", win_percentage)
        print("Loss percentage is ", loss_percentage)
        print("Win count is ", win_count)


if __name__ == "__main__":
    stake = float(input("Enter the stake you have: "))
    goal = float(input("Enter your goal amount: "))

    gamble = Gamble()
    gamble.gambling(stake, goal)

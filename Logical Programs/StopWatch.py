"""
    @Author: Ghouri Iqbal Khan
    @Date: 2022-07-12 23:45
    @Last Modified by: Ghouri Iqbal Khan
    @Last Modified time: 2022-07-12 23:45
    @Title : StopWatch
"""
import time


class Stopwatch:
    def watch(self):
        """
            Description:
                Calculating time with time in HH:MM:SS(Hours:Mins:Seconds)
            Parameter:
                passing second as a parameter
            Return:
                Returning Lapsed time and convert in the formate hours,mins and seconds.
        """

        try:

            while True:
                start = int(input("Enter 1 to Start:"))
                start_time = time.time()
                stop = int(input("Enter 0 to Stop Time:"))
                end_time = time.time()
                time_elapsed = end_time - start_time
                print("Time elapsed from Start to Stop is: ", time_elapsed, " Sec")
                check = int(input("1. Continue\n2.stop"))
                if check == 2:
                    break
        except ValueError:
            print(" Invalid input ")


if __name__ == '__main__':
    print("Welcome to Stopwatch")
    obj = Stopwatch()
    # calling Stopwatch function
    obj.watch()

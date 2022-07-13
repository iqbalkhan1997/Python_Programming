"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-12 15:42
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-12 15:42
@Title : Sum of three Integer adds to Zero.
"""


def find_triplets(arr, n):
    """
        Description:
            Finding Three numbers of combination on addition
        Parameter:
            Array and size of array
        Return:
            Printing Three numbers if it is in array
    """

    SumOfThreeNumbers = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    SumOfThreeNumbers = True

    if (SumOfThreeNumbers == False):
        print(" Triplets is not found ")


if __name__ == '__main__':
    while True:
        n = int(input("Enter Length Of An Array"))
        if n < 3:
            n = int(input("Enter Valid Length Of An Array"))
        else:
            arr = [n]
            break

    for i in range(n):
        print("Enter ", i, ": ")
        arr.append(int(input()))

find_triplets(arr, n)

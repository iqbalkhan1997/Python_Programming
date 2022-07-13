"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-12 14:57
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-12 14:57
@Title : Print 2D array
"""


def display_array(rows, columns):
    """
        Description:
            adding values in 2D Array
        Parameter:
            Rows and Columns
        Return:
            2D_Array values
    """

    row_values = []

    for i in range(0, rows):
        column_values = []
        for j in range(0, columns):
            print("Enter the {} {} th element".format(i, j))
            array_input = int(input())
            column_values.append(array_input)
        row_values.append(column_values)
    return row_values


if __name__ == "__main__":
    try:
        row = int(input("Enter number of rows : "))
        column = int(input("Enter number of columns : "))
        array_element = display_array(row, column)
        for i in range(len(array_element)):
            print(array_element[i])
    except Exception as e:
        print("Enter correct input", e)

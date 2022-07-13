"""
@Author: Ghouri Iqbal Khan
@Date: 2022-07-09 8:30
@Last Modified by: Ghouri Iqbal Khan
@Last Modified time: 2022-07-09 8:30
@Title : Printing the String Template with User Name
"""


def replace(user_name):
    """
        Description:
           Below function asks for the username and greet with the username
        Parameter:
            username must contain 3 character
        Return:
            String template with username
    """
    if len(user_name) < 3:
        return "Enter valid username of minimum 3 characters"
    else:
        return "Hello " + user_name + ", How are you?"


if __name__ == "__main__":
    user_name = input("Enter the user name: ")
    print(replace(user_name))

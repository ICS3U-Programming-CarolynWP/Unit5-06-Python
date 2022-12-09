# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/08
# Gets user information for a decimal and how many decimal
# Places they would like to round. Uses a function and passing by
# Reference to calculate the rounded number. Displays it back to user

# Function to round the decimal which was "passed by reference"
def round_decimal(given_decimal, round):
    rounded_number = 0
    # Calculating the rounded number
    rounded_number = given_decimal[0] * (10 ** (round))
    rounded_number = rounded_number + 0.5
    rounded_number = int(rounded_number)
    given_decimal[0] = rounded_number / (10 ** (round))


def main():

    # Title of the program
    print("Rounding Numbers\n")

    # User Inputs
    user_decimal_string = input("Please enter your decimal number: ")
    user_list = []
    user_rounding_string = input("Please enter how many decimal places: ")

    # Try Catch to make sure the inputs are valid
    try:
        user_decimal = float(user_decimal_string)
        user_rounding = int(user_rounding_string)
    except Exception:
        print("Please enter a valid number!")
    else:
        # To make sure the rounding number is positive
        if user_rounding < 0:
            print("You can only round to positive decimal places!")
        else:
            # Calling the function
            user_list.append(user_decimal)
            round_decimal(user_list, user_rounding)
            print(user_list)


if __name__ == "__main__":
    main()

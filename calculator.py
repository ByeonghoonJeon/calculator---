# 1. Greeting
number_dictionary = {}
print("Welcome to Jeon's calculator")
# 2. Ask and check the vlaidity of first number.
#   2-1. Build a function to check whether the input is valid number or not.
def check_number(initial_number):
    # (Decimal point and minus, plus symbol is removed to check if the input is only numbers.)
    number_to_list = list(initial_number)
    while "." in number_to_list:
        number_to_list.remove(".")
    while "," in number_to_list:
        number_to_list.remove(",")
    while "-" in number_to_list:
        number_to_list.remove("-")
    while "+" in number_to_list:
        number_to_list.remove("+")
    list_to_string = ""
    list_to_string = list_to_string.join(number_to_list)
    return list_to_string.isdigit()


# 5. Make functions for operation.
def add(x, y):

    return number_dictionary["initial_number"] + number_dictionary["next_number"]


def minus(x, y):
    return number_dictionary["initial_number"] - number_dictionary["next_number"]


def multiply(x, y):
    return number_dictionary["initial_number"] * number_dictionary["next_number"]


def division(x, y):
    return number_dictionary["initial_number"] / number_dictionary["next_number"]


while True:

    #   2-2. Request to input the first number.
    initial_number = input("Please input the first number.\n")

    #   2-3. Check if the number is valid.
    while check_number(initial_number) == False:
        initial_number = input("Please input numbers only\n")
    #  2-4. Add the initial number to the dictionary.
    number_dictionary["initial_number"] = float(initial_number)

    while True:

        # 3. Ask and check the validity of operation.
        operation = input("Please pick an operation. (/, *, +, -)\n")
        while operation not in ("/", "*", "+", "-"):
            operation = input(
                "Please pick an operation from the right side. (/, *, +, -)\n"
            )

        # 4. Ask next number and check its validity.
        next_number = input("Please input next number\n")
        while check_number(next_number) == False:
            next_number = input("Please input numbers only\n")
        next_number = float(next_number)

        #   4-1. Add the next number to the dictionary.
        number_dictionary["next_number"] = next_number

        # 6. Calculate with inputs. (initial_number, operation, next_number.) And add result to the dictionary.
        if operation == "+":
            print(
                f'Calculation: {number_dictionary["initial_number"]} + {number_dictionary["next_number"]}'
            )
            print(
                "Result:",
                add(
                    number_dictionary["initial_number"],
                    number_dictionary["next_number"],
                ),
            )
            number_dictionary["result"] = add(
                number_dictionary["initial_number"], number_dictionary["next_number"]
            )
        elif operation == "-":
            print(
                f'Calculation: {number_dictionary["initial_number"]} - {number_dictionary["next_number"]}'
            )
            print(
                "Result:",
                minus(
                    number_dictionary["initial_number"],
                    number_dictionary["next_number"],
                ),
            )
            number_dictionary["result"] = minus(
                number_dictionary["initial_number"], number_dictionary["next_number"]
            )
        elif operation == "*":
            print(
                f'Calculation: {number_dictionary["initial_number"]} X {number_dictionary["next_number"]}'
            )
            print(
                "Result:",
                multiply(
                    number_dictionary["initial_number"],
                    number_dictionary["next_number"],
                ),
            )
            number_dictionary["result"] = multiply(
                number_dictionary["initial_number"], number_dictionary["next_number"]
            )
        elif operation == "/":
            print(
                f'Calculation: {number_dictionary["initial_number"]} / {number_dictionary["next_number"]}'
            )
            print(
                "Result:",
                division(
                    number_dictionary["initial_number"],
                    number_dictionary["next_number"],
                ),
            )
            number_dictionary["result"] = division(
                number_dictionary["initial_number"], number_dictionary["next_number"]
            )

        # 7. Ask if they want to reset the result of continue with the output.
        reset_or_continue = input("Do you want to continue? Y/N\n")
        #   7-1. Check if the input is valid.
        while reset_or_continue.lower() not in ("y", "yes", "n", "no"):
            reset_or_continue = input(
                "Please type 'Y' if you want to continue or 'N' for reset the result."
            )
        # 8. If input is 'y' or 'yes', go to the line requesting to input the next_number.
        #   8.1 Replace initial_number in the dictionary with output value. and remove next_number in the dictionary.

        if reset_or_continue.lower() in ("y", "yes"):
            number_dictionary["initial_number"] = number_dictionary["result"]
            number_dictionary["next_number"] = ""
            number_dictionary["result"] = ""

            print(f'starting number is: {number_dictionary["initial_number"]}')
            continue
        elif reset_or_continue.lower() in ("n", "no"):
            print("See you again!")
            break
        break
    break
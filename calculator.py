def main():
    print("Simple Python Calculator")
    print("------------------------")

    current_result = None

    while True:
        try:
            if current_result is None:
                current_result = get_initial_operation()
            else:
                current_result = get_next_operation(current_result)

            print(f"Current result: {current_result}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            if not ask_restart():
                print("Exiting program...")
                break
            current_result = None
            continue

        if not ask_continue():
            print("Final result:", current_result)
            break


# -----------------------------
# Input Handling Functions
# -----------------------------

def get_initial_operation():
    number1 = get_number("Enter first number: ")
    operator = get_operator()
    number2 = get_number("Enter second number: ")

    result = calculate(number1, operator, number2)
    print(f"{number1} {operator} {number2} = {result}")
    return result


def get_next_operation(current_result):
    operator = get_operator()
    number2 = get_number("Enter next number: ")

    result = calculate(current_result, operator, number2)
    print(f"{current_result} {operator} {number2} = {result}")
    return result


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def get_operator():
    valid_operators = ["+", "-", "*", "/", "//", "%", "**"]

    while True:
        operator = input("Enter operator (+, -, *, /, //, %, **): ")
        if operator in valid_operators:
            return operator
        print("Invalid operator. Try again.")


# -----------------------------
# Calculation Logic
# -----------------------------

def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "//":
        return number1 // number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2


# -----------------------------
# Control Flow Helpers
# -----------------------------

def ask_continue():
    while True:
        answer = input("Do you want to continue? (Y/N): ").upper()
        if answer in ["Y", "N"]:
            return answer == "Y"
        print("Invalid input. Enter Y or N.")


def ask_restart():
    while True:
        answer = input("Do you want to restart? (Y/N): ").upper()
        if answer in ["Y", "N"]:
            return answer == "Y"
        print("Invalid input. Enter Y or N.")


# -----------------------------

if __name__ == "__main__":
    main()



def calculate_factorial(number_to_calculate_factorial: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    A factorial is the product of an integer and all the integers below it,
    e.g., 5! = 5 × 4 × 3 × 2 × 1 = 120

    Parameters:
        number_to_calculate_factorial (int): A non-negative integer

    Returns:
        int: The factorial of the input number
    """
    if number_to_calculate_factorial == 0:
        return 1

    factorial_result = 1
    for previous_num in range(1, number_to_calculate_factorial + 1):
        factorial_result *= previous_num
    return factorial_result


# User interaction
print("A factorial is the product of an integer and all the integers below it,\n"
      "e.g., 5! = 5 × 4 × 3 × 2 × 1 = 120")
print("This program calculates the factorial of a non-negative integer.")
try:
    user_input = int(input("\nEnter a non-negative integer: "))
    if user_input < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(user_input)
        print(f"The factorial of {user_input} is: {result}")
except ValueError:
    print("Invalid input. Please enter a whole number.")


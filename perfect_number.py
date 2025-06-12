

def find_perfect_number(given_number:int):
    """
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).

    :param given_number: receives an integer number
    :return: the following messages as string:
        "We have a perfect number!" - if the number is perfect.
        "It's not so perfect." - if the number is NOT perfect.
    """

    list_of_proper_positive_divisors:list = []
    for previous_num in range(1, (given_number//2) +1):
        if given_number % previous_num == 0:
            list_of_proper_positive_divisors.append(previous_num)
    # print(list_of_proper_positive_divisors)

    if sum(list_of_proper_positive_divisors) == given_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."



try:
    user_num:int = int(input("Enter a positive integer: "))
    if user_num <= 0:
        print("Perfect numbers must be positive integers greater than zero.")
    else:
        result = find_perfect_number(user_num)
        print(result)

except ValueError:
    print("Invalid input. Please enter a whole, positive number.")
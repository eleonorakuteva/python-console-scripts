

def password_report(password: str):
    """
    Analyzes a password string and returns a report on its content.
    The report includes:
    - Total length of the password
    - Number of digits
    - Number of special (non-alphanumeric) symbols
    - Whether it contains spaces
    - Whether it includes non-English letters
    - An estimated strength rating: Weak, Medium, or Strong.

    Strength criteria:
    - Weak: Fewer than 6 characters.
    - Medium: At least 6 characters and contains at least 2 of 3 types (digits, English letters, special symbols).
    - Strong: At least 10 characters and contains all 3 types (digits, English letters, special symbols).


    param: password:str -> The password string to be analyzed.
    return: A formatted string report summarizing the password analysis.
    """
    sum_of_numbers = 0
    sum_of_english_letters = 0
    sum_of_special_symbols = 0
    has_space = False
    has_non_english_letter = False

    for character in password:
        # detects for digits
        if character.isdigit():
            sum_of_numbers += 1
        # detects for only english letters
        elif character.isalpha():
            # detects for only english letters
            if character.isascii():
                sum_of_english_letters += 1
            # non-english letters
            else:
                has_non_english_letter = True
        # founds spaces
        elif character.isspace():
            has_space = True
        # detects special symbols
        elif not character.isalnum():
            sum_of_special_symbols += 1

    # Strength rating:
    total_length = len(password)
    strength = ""

    # It gives a score from 0 to 3 based on how many of the listed are non-zero.
    has_variety = sum(bool(x) for x in [sum_of_numbers, sum_of_english_letters, sum_of_special_symbols])
    if total_length < 6:
        strength = "Weak"
    elif total_length >= 6 and has_variety >= 2:
        strength = "Medium"
    if total_length >= 10 and has_variety == 3:
        strength = "Strong"

    report = ("--- Password Report ---\n"
              f"Total characters (length): {total_length}\n"
              f"Total digits: {sum_of_numbers}\n"
              f"Total special symbols: {sum_of_special_symbols}\n"
              f"Contains space? {'Yes' if has_space else 'No'}\n"
              f"Contains non-english letters? {'Yes' if has_non_english_letter else 'No'}\n"
              f"Estimated strength: {strength}")

    return report

user_input:str = input("Enter your password to receive a report: ")
result = password_report(user_input)
print(result)
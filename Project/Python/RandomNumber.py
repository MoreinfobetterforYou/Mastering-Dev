import random

def NumbersNotIncluded() -> list:
    """ This function asks the user for input about which numbers to exclude """
    numbers = []
    while True:
        number = input("What number do you want to exclude? \n (Type 'done' to exit) \n")
        if number.strip().lower() == "done":
            break
        if number.strip() != "":
            try:
                int(number)
            except ValueError:
                print("Please enter a valid number or 'done' to exit.")
                continue
            numbers.append(int(number))
    return numbers

def RandomNumberGenerator() -> str:
    """ This function generates random numbers between a minimum value and a maximum provided by the user, excluding the numbers provided by the user """
    while True:
        try:
            min_value = int(input("Enter the minimum value: "))
            max_value = int(input("Enter the maximum value: "))
            excluded_numbers = NumbersNotIncluded()
            numbers_to_generate = int(input("How many random numbers do you want to generate? "))
            if min_value >= max_value:
                print("Minimum value must be less than maximum value. Please try again.")
                continue
            if numbers_to_generate <= 0 or numbers_to_generate > (max_value - min_value + 1 - len(excluded_numbers)):
                print("\n ---------- Please enter a valid number of random numbers to generate, considering the range and excluded numbers. ---------- \n")
                continue
            break
        except ValueError:
            print("Please enter valid integers for minimum and maximum values.")

    random_numbers = []
    while len(random_numbers) < numbers_to_generate:
        random_number = random.randint(min_value, max_value)
        if random_number not in excluded_numbers and random_number not in random_numbers:
            random_numbers.append(random_number)
    return f"Generated random numbers: {random_numbers}"

result = RandomNumberGenerator()
print(result)
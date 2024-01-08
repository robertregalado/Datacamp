# import re

# def find_duplicate_digits(number):
#     str_number = str(number)
#     duplicates = re.findall(r'(\d)(?=.*\1)', str_number)
#     return list(set(duplicates)).sort()

# # Example usage
# number = int(input("Input a number: "))
# duplicates = find_duplicate_digits(number)
# print(f"The duplicate digits in {number} are: {', '.join(duplicates)}")


import re

def find_duplicate_digits(number):
    str_number = str(number)
    duplicates = re.findall(r'(\d)(?=.*\1)', str_number)
    duplicates = list(set(duplicates))  # Convert to set to remove duplicates
    duplicates.sort()  # Sort the list of duplicates
    return duplicates

# Example usage
number = int(input("Input a number: "))
duplicates = find_duplicate_digits(number)
print(f"The sorted duplicate digits in {number} are: {', '.join(duplicates)}")

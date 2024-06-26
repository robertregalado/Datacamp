"""
Creating a lambda function
"""

# Lambda average function
lambda x:sum(x) / len(x)

# x: arguments
# sum(x)/ len(x) -> expression

#  Get the average
(lambda x: sum(x) / len(x))([3,6,9])

#==========Storing and calling a lambda function============
# Store a lambda function as a variable
average = lambda x: sum(x) / len(x)

# Call the average function
average([3,6,9])

#===========Multiple Parameters====================

# Lambda function with two arguments
(lambda x,y: x**y)(2,3)

#=========Lambda functions with iterables==============
# .map() applies a function to all elements in an iterable

names = ["john", "sally", "leah"]
# Apply a lambda function inside map()
capitalize = map(lambda x: x.capitalize(), names)
print(capitalize) #<map object at 0x7fb200529c10>

# Convert to a list
list(capitalize) # ["John","Sally","Leah"]

#===============EXAMPLES===============
sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x*1.2)(sale_price))

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))


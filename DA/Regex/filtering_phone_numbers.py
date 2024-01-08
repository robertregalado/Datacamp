"""
Now, you need to write a script for a cell-phone searcher. It should scan a list of phone numbers and return those that meet certain characteristics.

The phone numbers in the list have the structure:

Optional area code: 3 numbers
Prefix: 4 numbers
Line number: 6 numbers
Optional extension: 2 numbers
E.g. 654-8764-439434-01.

You decide to use .findall() and the non-capturing group's negative lookahead (?!) and negative lookbehind (?<!).

The list cellphones, containing three phone numbers, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.
"""

"""
1. Get all cell phones numbers that are not preceded by the optional area code.
"""
import re

cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)

"""
2. Get all the cell phones numbers that are not followed by the optional extension.
"""

for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)
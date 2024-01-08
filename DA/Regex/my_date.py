import re

my_date = "Today is 23rd May 2019. Tomorrow  is 24th May 19."

regex = re.findall(r"(\d{2})(?:rd|th)", my_date)
print(regex)
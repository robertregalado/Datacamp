import re

my_string = "I want to have a pet. But I don't know if I want 2 cats, 1 dog or a bird."

regex = re.findall(r"(\d)+\s(cat|dog|bird)", my_string)
print(regex)
import re 

my_string = "John Smith: 34-34-34-042-980, Rebecca Smith: 10-10-10-434-425"

regex = re.findall(r"(?:\d{2}-){3}(\d{3}-\d{3})", my_string)
print(regex) 
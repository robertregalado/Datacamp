import re

text = 'Clary has 2 friends who she spends a lot time with.Susan has 3 brothers while John has 4 sisters.'

regex = re.findall(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', text)

#print(regex)

pets = re.findall(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', "Clary has 2 dogs but John has 3 cats")
#print(pets)
#print(pets[0][0])


username = re.search(r"(\d[A-Za-z])+", "My user name is 3e4r5fg")
#print(username)


my_string = "My lucky numbers are 875 and 323"

repeat_capturing_group = re.findall(r"(\d)+", my_string)
print(f"Repeat Capturing Group: {repeat_capturing_group}")

repeated_group = re.findall(r"(\d+)", my_string)
print(f"Repeated Group: {repeated_group}")
# Import date, timedelta
from datetime import date, timedelta

# Create dates

two_hurricanes_dates = [date(2016, 10, 7), date(2017, 6, 21)]
print("Year:", two_hurricanes_dates[0].year)
print("Month:", two_hurricanes_dates[0].month)
print("Day:", two_hurricanes_dates[0].day)
print("Weekday:", two_hurricanes_dates[0].weekday())

d1 = date(2017, 11, 5)
d2 = date(2017, 12, 4)
l = [d1, d2]
print("Mininum date:", min(l))

# Subtract two dates
delta = d2 - d1 

print("Delta Days:", delta.days)

# Create a 29 day timedelta
td = timedelta(days=29)
print(f"Time delta: {d1 + td}")

#====================================

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)

# ====================================

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}
# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)

#======================================

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])



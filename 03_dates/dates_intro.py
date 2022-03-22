# Dates are difficult to program with!
# - Timezones, Daylight Savings
# - Representation

# Time is usually calcuated using unix epoch
# with the format  January 1, 1970 00:00:00 UTC
# - UTC: Coordinated Universal Time, a time standard

# In Python, we use the datetime module by using an import
# to import datetime class and date class

from datetime import datetime, date

# Get current year, month and day
today=datetime.today()
print(f"today is {today}")

# Get the current year, month, day, hour, minute, second and millisecond

now =datetime.now()

print(f"the curent date and time is {now}")

# use the datetime constructor to build a specific date
someday = datetime(year=2022, month=11, day=11, hour=13)
print(f"the day is {someday}")

print(type(someday))

# day span between tow days
span =someday - datetime.now()

print(f"the day span is {span}")

print(type(span))
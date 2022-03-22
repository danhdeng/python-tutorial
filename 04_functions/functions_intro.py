# Functions in Python
# Define a block fo code that only runs when it is called
# Functions can be passed data as parameters
# Functions can return values
# white space is very important in Python!

# define a simple function
def print_name():
    my_name="Dan"
    print(my_name)


# call the simple function
print_name()

# A function take single parameter
def calculate_days_old(age_in_years):
    days_in_year =365
    age_in_days =age_in_years * days_in_year
    report =f"You are about {age_in_days} days old"
    print(report)

calculate_days_old(33)

# defined a function take single parameter
# return a value
def get_days_old(age_in_years):
    days_in_year =365
    return age_in_years * days_in_year

# run the funtion to get the days old return
days_old =get_days_old(28)

print(f"You are about {days_old} days old")


# A function take single parameter
# call other function
def calculate_days_old_call_other_func(age_in_years):
    age_in_days =get_days_old(age_in_years)
    report =f"You are about {age_in_days} days old"
    print(report)


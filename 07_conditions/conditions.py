# Conditional logic
# Allows us to make decisions based
# on the  truthiness of an expression

if 2>1:
    print("OK")

if 2<1:
    print("OK")
else:
    print("FOO")

# if -> else if -> else
if 2<1:
    print("OK")
elif 2 !=2:
    print("BAZ")
else:
    print("FOO")

if 1 < 2 and "a"=="a":
    print("All good")

# an empty list of "falsy"
errors =[]
if not errors:
    print("No error")


if not 0:
    print("Zero 0 is false")

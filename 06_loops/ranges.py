# Using range() 
# range() generates the integer numbers
# between the give start and stop value

# loop 3 times starting at 0
# note that range() does not include the lat number in the result
for i in range(3):
    print(f"we are in loop number: {i}")

# loop 4 times starting at 3
# note that range() does not include the lat number in the result
for i in range(3, 8):
    print(i)


# loop 4 times starting at 3, jumping by 2
# note that range() does not include the lat number in the result
for i in range(3, 13, 3):
    print(i)
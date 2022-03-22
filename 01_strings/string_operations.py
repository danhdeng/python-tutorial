# multiply strings
stars ="*" * 10
print(stars)

# length of string
my_string="length of string"
print(f"length of my_string is: {len(my_string)}")

# getting the index of a character 
# the starting index is from zero 0
index_of_g =my_string.index("g")
print(f"index of g is {index_of_g}") # result return 3

# upper case and lower case strings
language ="Python"
print(language.upper())
print(language.lower())

# Splitting a string on whitespace
# this will create a list of strings
sentence ="I am learning Python language"
words=sentence.split()
print(words)
#result ['I', 'am', 'learning', 'Python', 'language'] 
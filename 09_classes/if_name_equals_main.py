# when Python attempts to read a source file, the following happens:
# - the interpreter set a several variables, such as __name__
# - The interpreter Executes the code in the file


# from the python document:
# __main__ is the name of the scope in which top-level code executes
# from standard input, a script or from the interactive prompt.


# if you are running the code directly. e.g.
# > python yourfile.py
# Then the interpreter assigns the string '__main__' to
# the __name__ variable

# Otherwise, when a module is imported into a file, the __name__
#variable is set to the name of the imported module

# __main__ document reference
# https://docs.python.org/3/library/__main__.html 

import lunch_menu

cafe_menu=lunch_menu.LunchMenu()
cafe_menu.add_food("Sandwich")
cafe_menu.add_food("bagel")
cafe_menu.add_beverage('coffee')
cafe_menu.add_beverage('tea')

print("The Cafe Menu:")
cafe_menu.generate();


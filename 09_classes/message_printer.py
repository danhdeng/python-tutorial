# Classes provide a way to combine data with behavior,
# which is an representation of encapsulation.
# Classess allow us to create a new type to work with
# We can instantiate new instance of classess

class MessagePrinter:
    name = ''

    def __init__(self, name):
        self.name = name

    def print_hello(self):
        print(f'hello {self.name}')

    def print_hello_custom(self, custom_name):
        print(f'hello {custom_name}')
printer_1 =MessagePrinter("Dan")
printer_1.print_hello()

printer_2 =MessagePrinter("Bob")
printer_2.print_hello()
printer_2.print_hello_custom("Baz")
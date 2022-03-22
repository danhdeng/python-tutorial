# In Python, there are three types of numbers
# - int (integer) - No maximum
# - float (floating point numbers)
# - complex (complex numbers)

x = 12 # int
y =32.10 # float (beware of floating point errors!)
z =complex(2, 4) # complex number

print(f"integer: {x}, floating point number: {y}, complex number: {z}")

# Note that Boolean types are a subclass of numbers in Python
print(True==1) # True
print(False==0) # True
print (True + True + True) # 3
print(True/False) # ZeroDivisionError 

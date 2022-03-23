# Lists are ordered collections of any type of object

# List of email strings collection starting with index 0
emails =[
    "test@test.com", # index 0
    "foo@boo.com", # index 1
    "far@example.com" # index 2
]

index_0=emails[0]
index_1=emails[1]
index_2=emails[2]

print(f"index_0: {index_0}\nindex_1: {index_1}\nindex_2: {index_2}" )

#operations on the lists
#combining, appending, Extending, Inserting, Removing, Popping from lists

# Augmented Assignment
emails +=["test@abc.com", "abc@cbc.com"]
print(emails)

# list concatenation
scores=[1, 2, 3] + [4, 5] + [6]
print('intial concatenated scores', scores)

#modify a list in place
scores.append(7)
print("scores after appending 7:", scores)

# extend the list 
scores.extend([8, 9])
print("scores after extending [8, 9]:", scores)

# remove item at index 0
result=scores.pop(5)
print("the remove item is:", result)
print("score after removing the fifth item:", scores)

# insert item into the list in index 4
scores.insert(4, "newInsert")
print("score after inserting item in index 4:", scores)

# remove item from the list with item value
scores.remove("newInsert")
print("score after removing item in index 4:", scores)

# Get the size of the  list
list_length=len([1,2,3,4,5]);

print(f"the size of the list is {list_length}")

# getting the maximum and minimum values of a list
my_num_list=[23, 45, 66, 12, 88]

list_max=max(my_num_list)
list_min=min(my_num_list)

print(f"maximum value is: {list_max} and minimum value is: {list_min} in my_num_list")

# slciing lists
# some_list[a:b] +. get some part of a the list
# starting from a to b , non-inclusive to b
steps=[
    'wake up',
    'get out of bed',
    'make coffee',
    'brush teeth',
    'go for walk',
    'start to work'
]

print('steps are: ', steps)
print('steps[0:2] are: ', steps[0:2]) # get the first two steps
print('steps[0:] are: ', steps[0:])  # get the entire list
print('steps[:4] are: ', steps[:4]) # get the first four steps


# specify the stride as the third colon-separated element of a slice
print('steps[0:4:2] are: ', steps[0:4:2])
print('steps[0::1] are: ', steps[0::1])

# reverse a list
print(f'Reversing stpes with steps[::-1]: ',steps[::-1])

# reverse a string
print('this is an example'[::-1])

# strings and lists are both iterables

hello="hello"
some_list=['h','e','l','l','o']

# string slicing is reference to the same object
print(hello is hello[:])  #=> True

#list slcing will create a new object which is the reference is not the same
print(some_list is  some_list[:]) # => False

# Nesting Lists
matrix =[[1,2,3],
        [4, 5, 6],
        [7, 8, 9]]
jagged_list=[[1],
            [2,3],
            [-4],
            [0, 3, 0, -1]]
nested_list=[[1],
             [2,3,[4,5,6]]]

print(matrix[0][1])
print(jagged_list[2][0])
print(nested_list[1][2][0])

# use the for loop to print out the matrix
for element in matrix:
    print(element)
    
# Tuples

# Tuples are immutable!

x =('foo', 'bar', 'baz')
y =['foo', 'bar', 'baz']
print(type(x), type(y))

#x[0]='quck' # raise error: TypeError: 'tuple' object does not support item assignment


# iterate the tuples

print(x[::-1])

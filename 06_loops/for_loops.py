# for loops in Python
# - Iterate over a sequence
# -  list, tuple, dictionary, string
# - it acts like "for each element in iterable"

# mindful loop

things_i_see=["plant", "grass", "laptop", "windows", "tree"]
for thing in things_i_see:
    print(thing)


numbers=[1, 23, 45, 34, 28]

#print each number in numbers
for n in numbers:
    print(n)

# calculate the total of numbers
total_sum=0
for n in numbers:
    total_sum +=n
    print(total_sum)

# looping through a dictionary

user ={
    "name": "Foo",
    "age": 64,
    "email": "foo@trest.com"
}

for key in user:
    print(f"Key: {key}\t => \tvalue: {user[key]}")
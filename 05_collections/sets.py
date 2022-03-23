# Sets in Python are:
# - Unordered
# - Contain distinct elements
# - Contain only hashable types
# - strings, numbers, some collections if their elements ar hashable
# - NOT dictionaries or lists for instance.

# using the set literal syntax
colors_1={"blue", 'green', 'yellow','red'}
print(colors_1)

# Use set() instead of
user_ids=set([123, 433, 222, 222, 333, 333, 333,433])
print(user_ids) # output {433, 123, 333, 222} only can contain distinct number

# use set to determine the unique number of elements in the list
number_unique_users=len(user_ids)
print(f"total unique user id is:{number_unique_users}")

# use set to break down the sentence into unique characters
sentence="I am learning python language..."
print(set(sentence))

# Set can contain different types of elements
sample_set={123, True, "bar"}
print(sample_set)

# Set operations

# union operator represented by |
s1={1,2,3}
s2 ={4,5,6}
s3=s1 | s2
print("Union of s1 |s2", s3)

# intersections operator represented by &
# or use set.intersection function
s1={1,2,3}
s2 ={3,4,5,6}
s3=s1 & s2
print("Intersection of s1 |s2", s3)
print("Intersection of s1.intersection(s2)", s1.intersection(s2))

# difference operator represented by -
# set.difference function
s1={1,2,3}
s2 ={3,4,5,6}
s3=s1 - s2 
print("difference of s1-s2", s3)
print("difference of s1.difference(s2)", s1.difference(s2))

# symmetric difference operator represented by ^
# set.difference function
s1={1,2,3}
s2 ={3,4,5,6}
s3=s1 ^ s2 
print("symmetric difference of s1^s2", s3)

drinks={"water", "tea", "coffee"}
drinks.add("mineral water")
drinks.remove("water")
#drinks.remove("wine") # throw a type error (KeyError: 'wine') if wine does not exit in the set.
drinks.discard("wine") #does nothing if wine does not exist in the set
print(drinks)

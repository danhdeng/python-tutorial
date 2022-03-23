# Dictionaries in Python are:
# - Unordered
# - can be changed by
# - access value by key with key-value pair
# - sometimes called an associative array or hash table in other languages

# build a dictionary

customer_address={
    "id"            : 11,
    "street"        : "123 test road",
    "city"          : "Toronto",
    "province"      : "Ontario",
    "postal_code"    : "M4M2G5",
    "is_active"     : True,
}

# accessing the value by key
city=customer_address["city"]
is_active=customer_address["is_active"]

print(f"City: {city}, active: {is_active}")

# assign a new value to an existing key
customer_address["city"]="Montreal"
print(f"new cusomter city: {customer_address['city']}")

# adding new key value pair to the dictionary
customer_address["phone_number"]="555-555-5656"

print(f"cusomter's phone_number: {customer_address['phone_number']}")

# nested dictionary

customer={
    "name"          : "Jane Doe",
    "age"           : 56,
    "is_employee"   : True,
    "address"       : customer_address
}

# accessing the nested dictionary by key

print(f"cusotmer located at the province is: {customer['address']['province']}")
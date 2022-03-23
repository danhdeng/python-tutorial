# write a dictionary as JSON to a file

import json

list_of_names={
    1: 'Jimmy',
    2: "Jan",
    3: 'Rob',
    4: "Doe"
}

# Open a new file in write mode and save the dictionary as JSON
with open('./list_of_name.json', 'w') as f:
    json_data=json.dumps(list_of_names)
    f.write(json_data)
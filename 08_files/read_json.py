# Read Json data from file and load into dictionary
import json

def read_my_json():
    with open('./list_of_name.json', 'r') as f:
        my_data=json.load(f)
        print(type(my_data))

        # print the key value pairs of the dictionary
        for key, val in my_data.items():
            print(key, val)

with open('./sample_data/sample.json', 'r') as f:
    sample_data=json.load(f)
    for obj in sample_data['dataset']:
        title=sample_data['dataset'][obj].get('title')
        print(title)
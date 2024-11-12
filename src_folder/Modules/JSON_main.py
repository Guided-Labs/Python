## JSON Module

import json

def convert_dict_to_json(data):
    """Convert a Python dictionary to a JSON string."""
    return json.dumps(data)

data = {"name": "Alice", "age": 30}
json_data = convert_dict_to_json(data)
print(json_data) 
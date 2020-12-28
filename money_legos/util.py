import json


def read_json(file_location):
    json_data = None
    with open(file_location, "r") as json_file:
        json_data = json_file.read()
    return json.loads(json_data)
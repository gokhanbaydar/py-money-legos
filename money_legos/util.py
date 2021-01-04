import json
import pkgutil


def read_json(file_location):
    return json.loads(pkgutil.get_data(__package__, file_location))

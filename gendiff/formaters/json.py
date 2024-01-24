"""Function for displaying differences in a json format"""

import json


def to_json(diff):
    return json.dumps(diff, indent=4)

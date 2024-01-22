"""Function for displaying differences in a json format"""

import json


def to_json(tree):
    """
    Difference output in json format.
    The argument tree is difference tree of two files.
    """

    return json.dumps(tree, indent=2)

"""Finding differences between two dictionaries."""


def build_diff(old, new):
    """
    Takes two dictionaries as arguments and finds differences between them.
    The argument first_dict is first dictionary.
    The argument second_dict is second dictionary.
    Returns a tree of differences.
    """

    res = {}
    keys = set(new.keys()) | set(old.keys())
    keys = sorted(keys)
    for key in keys:
        if key not in new:
            res[key] = {'type': 'removed', 'value': old[key]}
            continue
        if key not in old:
            res[key] = {'type': 'added', 'value': new[key]}
            continue
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            res[key] = {
                'type': 'nested_dict', 'value': build_diff(old[key], new[key])
            }
            continue
        if old[key] != new[key]:
            res[key] = {
                'type': 'updated', 'old_value': old[key],
                'new_value': new[key]
            }
            continue
        res[key] = {'type': 'same', 'value': old[key]}
    return res

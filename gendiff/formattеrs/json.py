import json


def create_json(diff_list):
    """Convert diff list to JSON string."""
    return json.dumps(diff_list, indent=4)

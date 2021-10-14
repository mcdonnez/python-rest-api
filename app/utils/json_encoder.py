"""Custom JSON Encoder to convert snake_case properties to camelCase json"""
import json


def to_camel_case(snake_str):
    """converts snake_case to camelCase"""
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

# pylint: disable=invalid-name
def json_camel_case(o):
    """convert dict with snake_case to json dict with camelCase"""
    json_dict = {}
    for key, value in o.__dict__.items():
        json_dict[to_camel_case(key)] = value
    return json_dict


class CamelCaseEncoder(json.JSONEncoder):
    """Special encoder that converts snake_case to camelCase for json output"""

    def default(self, o):
        """default method to convert to camelCase"""
        return json_camel_case(o)

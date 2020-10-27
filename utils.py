import json


def printjson(inline_json, returnOnly=False):
    format_json = json.dumps(inline_json, indent=4, sort_keys=True)
    if returnOnly:
        return format_json
    print(format_json)

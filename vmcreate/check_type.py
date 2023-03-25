import sys
import json

def check_type(type=None):
    supports = json.loads(open("template_dict.json", "r").read())
    if type is None:
        print("Error: VM type is needed, Please define a type of the VM.")
        sys.exit()
    elif type not in supports.keys():
        print(
            f"Error: {type} is not supported, Use --vmlist to show the list of the VM."
        )
        sys.exit()
    else:
        return type
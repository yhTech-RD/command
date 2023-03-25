import sys
import json


def print_option_list():
    supports = json.load(open("template_dict.json", "r"))
    print("\n".join(list(supports.keys())))
    sys.exit()


if __name__ == "__main__":
    print_option_list()

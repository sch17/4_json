import json
from sys import argv

def load_data(filepath):
    with open(filepath, 'r', encoding="utf8") as input_file:
        json_data = json.load(input_file)
    return json_data


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    filepath = argv[1]
    pretty_print_json(load_json_file(filepath))

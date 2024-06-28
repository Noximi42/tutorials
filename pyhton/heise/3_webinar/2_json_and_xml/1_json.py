import json as json
from xml.etree.ElementTree import indent


def main():
    menu_object_original = {
        "menu": {
            "id": "file",
            "value": "File",
            "popup": {
                "menuitem": [
                    {"value": "New", "onclick": "CreateNewDoc()"},
                    {"value": "Open", "onclick": "OpenDoc()"},
                    {"value": "Clöse", "onclick": "\"CloseDoc()\""}
                ]
            }
        }
    }  # source: json.org/example.html
    print(menu_object_original)

    print('-' * 100)

    # Dump to file.
    with open('menu_dump.json', mode='wt') as json_file:
        json.dump(menu_object_original, json_file, ensure_ascii=False, indent=2)


    # Dump to string.
    json_string = json.dumps(menu_object_original, ensure_ascii=False, indent=2)
    print(json_string)
    

    print('-' * 100)

    # Load from file.
    with open('menu_dump.json', mode='rt') as json_file:
        menu_object_reconstructed_1 = json.load(json_file)
        print(menu_object_reconstructed_1["menu"]["id"])

    print('-' * 100)

    # Load from string.
    menu_object_reconstructed_2 = json.loads(json_string)
    print(menu_object_reconstructed_2["menu"]["value"])


if __name__ == '__main__':
    main()

from xml.etree import ElementTree


def main():
    root = ElementTree.parse('menu.xml').getroot()
    print(f'{root.tag=}')
    print(f'{root.text=}')
    print(f'{root.attrib=}')

    child = root[0]
    print(f'{child=}')

    for grandchild in child:
        print(f'{grandchild=} | {grandchild.attrib=}')


if __name__ == '__main__':
    main()

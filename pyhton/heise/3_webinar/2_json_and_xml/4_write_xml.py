from xml.etree import ElementTree


def main():
    root = ElementTree.Element('menu', {'id': 'file', 'value': 'File'})
    child = ElementTree.SubElement(root, 'popup')
    ElementTree.SubElement(child, 'menuitem', {'value': 'New', 'onclick': 'CreateNewDoc()'})
    ElementTree.SubElement(child, 'menuitem', {'value': 'Open', 'onclick': 'OpenDoc()'})
    ElementTree.SubElement(child, 'menuitem', {'value': 'Close', 'onclick': 'CloseDoc()'})

    ElementTree.indent(root)
    ElementTree.ElementTree(root).write('menu_dump.xml')
    print(ElementTree.tostring(root, encoding='unicode'))


if __name__ == '__main__':
    main()

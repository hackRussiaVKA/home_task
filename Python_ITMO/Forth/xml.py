import xml

from xml.etree import ElementTree

root = ElementTree.parse('xml')
root = root.getroot()
for a in root:
    print(root)

# get_attr_number counts the attributes on a node and recursively adds the attribute
# counts of all of its children.

import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)

    for child in node:
        score += get_attr_number(child)
    return score

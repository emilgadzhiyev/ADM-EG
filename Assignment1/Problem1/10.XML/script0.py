# XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

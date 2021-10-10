# XML2 - Find the Maximum Depth

maxdepth = 0


def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)

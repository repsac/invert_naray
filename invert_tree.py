"""
Given a tree structure, take the values and invert them left to right.
Since the group (graph, tree, etc) can be arbitrary,
like the example below, it can't be effectively represented
in a flat list like a binary tree example

            0
          / | \
         /  |  \
        1   2   3
       /|\       \
      / | \      /\
     6  7  8    9 10
                  /\
                 /  \
                11  12

The aforementioned tree is expressed in nested tuples.
Any index that has it's own children will be wrapped
in its own tuple where the first index is the node and
the second is reserved for the children

Here is an example tree represented in tuples
(0, ((1, (6, 7, 8)), 2, (3, (9, (10, (11, 12))))))

The resulting tree would then look like
            0
          / | \
         /  |  \
        3   2   1
       /\      /|\
      /  \    / | \
     10   9  8  7  6
     /\     
    /  \ 
   12  11
"""


def invert(tree):
    """
    Inverts non-binary trees using a nested tuple structure

    :param tuple tree: the n-aray to invert
    :rtype: tuple
    :returns: the inverted tree
    """
    root = _test_for_root(tree, None)

    return root.reverse()


def _test_for_root(data, parent):

    def issubtree(x):
        return isinstance(x[0], int) and isinstance(x[1], tuple)

    root = None
    if len(data) == 2 and issubtree(data):
        root = Node(data[0], parent=parent)
        _parse_tree(data[1:], root)
    else:
        _parse_tree(data, parent)

    return root


def _parse_tree(tree, parent):
    for each in tree:
        if isinstance(each, int):
            Node(each, parent=parent)
        elif isinstance(each, (tuple, list)):
            _test_for_root(each, parent)
        else:
            error = "Unknown data type '{}' for {}".format(
                type(each), str(each))
            raise ValueError(error)


class Node(object):
    def __init__(self, value, children=None, parent=None):
        self.value = value
        self.children = children or []
        self.parent = parent
        if self.parent is not None:
            self.parent.children.append(self)

    def reverse(self):
        reversed_children = []
        for child in reversed(self.children):
            if child.children:
                reversed_children.append((child.value, child.reverse()))
            else:
                reversed_children.append(child.value)
        result = tuple(reversed_children)
        if self.parent is None:
            result = (self.value, result)
        return result

    def __repr__(self):
        return '{} => [{}]'.format(self.value, self.children)

    def __str__(self):
        return self.__repr__()
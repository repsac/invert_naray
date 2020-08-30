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


VALID_ARRAY_TYPES = (tuple,)


def invert(tree):
    """
    Inverts non-binary trees using a nested tuple structure

    :param tuple tree: the non-binary array to invert. binary arrays can be supported
    :rtype: tuple
    :returns: the inverted tree
    """
    return _test_for_root(tree, None).reverse()


def binarytree_to_graph(binary_array):
    """
    Takes in a flat array, typical in binary arrays, and formats the
    data into a graphed array that is compatible with this library

    :param [] binary_array: standard binary array
    :rtype: ()
    :returns: formatted graph (1, (...), (...), (...))
    """
    root = Node(binary_array[0], None)
 
    def sort_branches(x, y, parent):

        def split_branch(x, y, parent):
            try:
                parent = Node(binary_array[x], parent)
            except IndexError:
                pass
            else:
                x = x+y
                y *= 2
                sort_branches(x, y, parent)
        
        split_branch(x, y, parent)
        split_branch(x+1, y+1, parent)

    sort_branches(1, 2, root)

    return root.dump()


def _test_for_root(data, parent):
    """
    A root array has only two indices. The first is an <int> and the second
    is a valid array (see constant above) that contains node data about
    children branches.

    If the data is not recognized as a root array then it may just be an
    array listing the nodes at that particular scope. Each node may or
    may not have children, but that is determined in _parse_scope()

    :param () data: this data could be any combination <int> and valid arrays
                    Examples:
                        (<int>, (..)) <-- valid subtree root
                        (<int>, <int>, ..)
                        (<int>, (..), <int>)
                        ((..), <int>, (..))
                        etc
    :param Node() parent: parent node of the current tree level
    """

    def issubtree(x):
        """
        looking for a tuple that matches (<int>, (...))
        """
        return len(data) == 2 and (isinstance(x[0], int) and 
                                   isinstance(x[1], VALID_ARRAY_TYPES))

    root = None

    if issubtree(data):
        root = Node(data[0], parent)
        _parse_scope(data[1], root)
    else:
        _parse_scope(data, parent)

    return root


def _parse_scope(scope, parent):
    """
    Parse a particular scope of the tree. The scope can have any
    combination of <int> or nested tuples.

    If a single <int> is found, then that node is the end of the branch
    Otherwise, a tuple indicates a node that has children nodes

    :param () scope:
    :param Node() parent:
    """
    for each in scope:
        if isinstance(each, int):
            Node(each, parent)
        elif isinstance(each, VALID_ARRAY_TYPES):
            _test_for_root(each, parent)
        else:
            error = "Unknown data type '{}' for {}".format(
                type(each), str(each))
            raise ValueError(error)


class _return(object):
    """
    Decorator for managing the return states of public Node methods
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, method):

        def wrapped(node_inst):
            return node_inst._children(self.func, method.__name__)

        return wrapped


class Node(object):
    def __init__(self, value, parent):
        """
        Each index/<int> is identified as a unique node, and represented
        by an instance of Node()

        :param int value: The value this instance represents
        :param Node() parent: The parent node, may be None if it's the root
        """
        self.value = value
        self.children = []
        self.parent = parent
        if self.parent is not None:
            self.parent.children.append(self)

    @_return(lambda x: x)
    def dump(self):
        """
        Dumps the current node, and it's children, to formatted
        tuple with nested tuples to graph the hierarchy.

        :rtype: ()
        """
        pass
    
    @_return(reversed)
    def reverse(self):
        """
        Reverses, from left to right, and dumps the current node,
        and it's children, to formatted tuple with nested tuples
        to graph the hierarchy.

        :rtype: ()
        """
        pass
    
    def _children(self, func, method):
        """
        :param def() func:
        :param self.method() method:
        :rtype: ()
        """
        children = []
        for child in func(self.children):
            if child.children:
                children.append((child.value, getattr(child, method)()))
            else:
                children.append(child.value)
        result = tuple(children)
        if self.parent is None:
            result = (self.value, result)
        return result
"""
    def __repr__(self):
        return '{} => [{}]'.format(self.value, self.children)

    def __str__(self):
        return self.__repr__()"""
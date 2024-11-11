# This problem was asked by Google.

# Invert a binary tree.

# For example, given the following tree:

#     a
#    / \
#   b   c
#  / \  /
# d   e f
# should become:

#   a
#  / \
#  c  b
#  \  / \
#   f e  d


from typing import Optional

class Node:
    def __init__(self, val: str):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def invert(node: Node) -> Node:
    tmp = node.left
    node.left = invert(node.right) if node.right else None
    node.right = invert(tmp) if tmp else None
    return node



tree = Node("a")
tree.left = Node("b")
tree.left.left = Node("d")
tree.left.right = Node("e")
tree.right = Node("c")
tree.right.left = Node("f")

inverted = invert(tree)
assert(inverted.val == "a")
assert(inverted.left.val == "c")
assert(inverted.left.right.val == "f")
assert(inverted.right.val == "b")
assert(inverted.right.left.val == "e")
assert(inverted.right.right.val == "d")

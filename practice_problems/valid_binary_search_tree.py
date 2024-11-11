# This problem was asked by LinkedIn.

# Determine whether a tree is a valid binary search tree.

# A binary search tree is a tree with two children, left and right,
# and satisfies the constraint that the key in the left child must be less than or equal to
# the root and the key in the right child must be greater than or equal to the root.
from typing import Any, Dict, Optional

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def valid_binary_search_tree(node: Node) -> bool:
    if node.left:
        if node.left.value > node.value:
            return False
        if not valid_binary_search_tree(node.left):
            return False
    if node.right:
        if node.right.value < node.value:
            return False
        if not valid_binary_search_tree(node.right):
            return False
    return True


root = Node(10)
root.left = Node(4)
root.right = Node(100)
assert(valid_binary_search_tree(root))

root.left.right = Node(5)
assert(valid_binary_search_tree(root))

root.right.right = Node(11)
assert(not valid_binary_search_tree(root))

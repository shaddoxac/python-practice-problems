# This problem was asked by Google.

# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.

# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

from typing import Optional

class Node:
    def __init__(self, val: str):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def is_subtree(subtree, tree) -> bool:
    if compare_binary_trees(subtree, tree):
        return True
    return compare_binary_trees(subtree, tree.left) or compare_binary_trees(subtree, tree.right)

def compare_binary_trees(subtree, tree) -> bool:
    if not subtree:
        return tree is None
    if not tree:
        return False
    if subtree.val == tree.val:
        return compare_binary_trees(subtree.left, tree.left) and compare_binary_trees(subtree.right, tree.right)
    return False



tree = Node("a")
tree.left = Node("b")
tree.left.left = Node("d")
tree.left.right = Node("e")
tree.right = Node("c")

subtree = Node("b")
subtree.left = Node("d")

assert(not is_subtree(subtree, tree))

subtree.right = Node("e")
assert(is_subtree(subtree, tree))

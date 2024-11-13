# This problem was asked by Google.

# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

# For example, given the following tree and K of 20

#     10
#    /   \
#  5      15
#        /  \
#      11    15
# Return the nodes 5 and 15.

from typing import Optional, Set, Tuple


class Node():
    def __init__(self, val):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def get_tree_sum(root: Node, k: int) -> Tuple[int, int]:
    if not root:
        return (-1, -1)
    to_process = [root]
    looking_for: Set[int] = set()
    while to_process:
        cur_node = to_process.pop()
        difference = k - cur_node.val
        if difference in looking_for:
            return (difference, cur_node.val)
        else:
            looking_for.add(difference)
        if cur_node.left:
            to_process.append(cur_node.left)
        if cur_node.right:
            to_process.append(cur_node.right)
    return (-1, -1)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(11)
root.right.right = Node(15)

assert(get_tree_sum(root, 20) == (5, 15))

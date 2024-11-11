# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.

from typing import Dict, List, Tuple, Optional

class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def get_level_sum(root: Node) -> Dict[int, int]:
    levels: Dict[int, int] = {}
    to_process: List[Tuple[Node, int]] = [(root, 0)]

    while to_process:
        (current_node, level) = to_process.pop()
        if level in levels:
            levels[level] += current_node.val
        else:
            levels[level] = current_node.val

        if current_node.left:
            to_process.append((current_node.left, level+1))
        if current_node.right:
            to_process.append((current_node.right, level+1))
    return levels
        

def get_minimum_sum(root: Node) -> int:
    level_sums = get_level_sum(root)
    ret = 0
    min_found = 999999999
    for (key, value) in level_sums.items():
        if value < min_found:
            min_found = value
            ret = key
    return ret

root = Node(
    val=1,
    left=Node(-2),
    right=Node(-3, Node(4), Node(-5))
)
assert(get_minimum_sum(root) == 1)


root2 = Node(
    val=1,
    left=Node(2, Node(4), Node(5, Node(-1))),
    right=Node(
        val=3,
        right=Node(6, Node(-7), Node(-8))
    )
)

assert(get_minimum_sum(root2) == 3)
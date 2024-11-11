# This problem was asked by Google.

# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

#     a
#    / \
#   b   c
#  /
# d


from typing import Optional, Tuple

class Node:
    def __init__(self, val: str):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def deepest_helper(node: Node, depth: int = 0) -> Tuple[str, int]:
    if node.left and node.right:
        l = deepest_helper(node.left, depth+1)
        r = deepest_helper(node.right, depth+1)
        if l[1] > r[1]:
            return l
        return r
    elif node.left:
        return deepest_helper(node.left, depth+1)
    elif node.right:
        return deepest_helper(node.right, depth+1)
    else:
        return (node.val, depth)
    
def deepest(node: Node) -> str:
    return deepest_helper(node)[0]


tree = Node("a")
tree.left = Node("b")
tree.left.left = Node("d")
tree.right = Node("c")

t: Tuple[str, int] = ("a", 1)


assert deepest(tree) == "d"

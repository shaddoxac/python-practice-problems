# Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

# For example, the inorder successor of 22 is 30.

#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.

from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, left: "Node"):
        self.left = left
        self.left.parent = self

    def set_right(self, right: "Node"):
        self.right = right
        self.right.parent = self


def inorder_next(root: Node, val) -> Optional[Node]:
    if not root:
        return None
    if val == root.val:
        return get_next(root)
    # haven't found the value yet, keep looking
    elif val < root.val:
        return inorder_next(root.left, val)
    else: # must be greater
        return inorder_next(root.right, val)



def get_next(node: Node) -> Optional[Node]:
    if node.right:
        cur_node = node.right
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node
    # nothing to the right
    elif node.parent and node.parent.left == node: # check if there is a parent and this is left of it
        return node.parent
    else: # there is no 'next' element if there is nothing to the right or above
        return None

    

root = Node(10)
root.set_left(Node(5))
root.set_right(Node(30))
root.right.set_left(Node(22))
root.right.set_right(Node(35))

assert(inorder_next(root, 22).val == 30)
assert(inorder_next(root, 5).val == 10)
assert(inorder_next(root, 4) == None)
assert(inorder_next(root, 35) == None)

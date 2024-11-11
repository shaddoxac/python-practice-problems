# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

from typing import List, Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def toString(self):
        ret = f"{self.value}\n"
        if self.left:
            ret += f"{self.left.toString()}"
        if self.right:
            ret += f"{self.right.toString()}"
        return ret

def create_tree(preorder, inorder):
    if not preorder:
        return None
    
    root = Node(preorder[0])
    preorder = preorder[1:]

    if not preorder:
        return root

    root_index = inorder.index(root.value)
    inorder_left = inorder[:root_index]
    inorder_right = inorder[root_index+1:]

    
    if inorder_left:
        root.left = create_tree(preorder[:root_index], inorder_left)

    if inorder_right:
        root.right = create_tree(preorder[root_index:], inorder_right)

    return root
    

def preorder_from_tree(n: Node) -> List:
    ret = []

    if not n:
        return ret
    
    ret += n.value

    if n.left:
        ret += preorder_from_tree(n.left)
    
    if n.right:
        ret += preorder_from_tree(n.right)

    return ret

def inorder_from_tree(n: Node) -> List:
    ret = []

    if not n:
        return ret
    
    if n.left:
        ret += inorder_from_tree(n.left)
    
    ret += n.value

    if n.right:
        ret += inorder_from_tree(n.right)

    return ret

print(create_tree(["a", "b", "d", "e", "c", "f", "g"], ["d", "b", "e", "a", "f", "c", "g"]).toString())

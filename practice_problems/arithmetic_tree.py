# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def compute(self):
        if self.val == "+":
            return self.left.compute() + self.right.compute()
        elif self.val == "-":
            return self.left.compute() - self.right.compute()
        elif self.val == "*":
            return self.left.compute() * self.right.compute()
        elif self.val == "/":
            return self.left.compute() / self.right.compute()
        else:  # assume numeric
            return int(self.val)
        

root = Node("*")
root.left = Node("+")
root.left.left = Node(3)
root.left.right = Node(2)
root.right = Node("+")
root.right.left = Node(4)
root.right.right = Node(5)

assert(root.compute() == 45)

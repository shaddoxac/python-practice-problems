# Implement a stack that has the following methods:

#   push(val), which pushes an element onto the stack

#   pop(), which pops off and returns the topmost element of the stack.
#          If there are no elements in the stack, then it should throw an error or return null.

#   max(), which returns the maximum value in the stack currently.
#          If there are no elements in the stack, then it should throw an error or return null.

# Each method should run in constant time.

from typing import Optional

class Stack():
    def __init__(self):
        self.stack = []
        self.maximum: Optional[int] = None
        # self.value_map = {}
    
    def push(self, val: int):
        self.stack.append(val)
        if self.maximum is not None or val > self.maximum:
            self.maximum = val

        # if val in self.value_map:
        #     self.value_map[val] += 1
        # else:
        #     self.value_map[val] = 1

    def pop(self) -> Optional[int]:
        if not self.stack:
            return None
        
        return_val = self.stack[-1]
        self.stack = self.stack[:-1]
        # if self.value_map[return_val] == 1:
        #     del self.value_map[return_val]
        # else:
        #     self.value_map[return_val] -= 1
        return return_val

    def max(self) -> Optional[int]:
        return self.maximum
        



s = Stack()
s.push(1)
s.push(200)
s.push(2)
assert(s.max() == 200)
assert(s.pop() == 2)
assert(s.max() == 200)
assert(s.pop() == 200)
s.push(0)
assert(s.max() == 1)
assert(s.pop() == 0)
assert(s.pop() == 1)
assert(s.pop() is None)

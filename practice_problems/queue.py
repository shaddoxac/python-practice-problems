# Implement a queue using two stacks.
# Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
# enqueue, which inserts an element into the queue, and
# dequeue, which removes it.


class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.values:
            return None
        ret = self.values[-1]
        self.values = self.values[:-1]
        return ret
    
    def is_empty(self):
        return len(self.values) == 0
    
class Queue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def enqueue(self, value):
        if self.pop_stack.is_empty():
            self.pop_stack.push(value)
        else:
            self.push_stack.push(value)

    def dequeue(self):
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()
    

q = Queue()
q.enqueue(1)
assert(q.dequeue() == 1)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
assert(q.dequeue() == 1)
assert(q.dequeue() == 2)
assert(q.dequeue() == 3)


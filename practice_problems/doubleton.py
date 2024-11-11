# This problem was asked by Microsoft.

# Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
# And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.

class Instance:
    def __init__(self, id):
        self.id = id

class Doubleton:
    def __init__(self):
        self._instance1 = Instance(1)
        self._instance2 = Instance(2)
        self.counter = 0

    @property
    def getInstance(self):
        if self.counter % 2 == 0:
            ret = self._instance1
        else:
            ret = self._instance2
        self.counter += 1
        return ret
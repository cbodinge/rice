class _QS:
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self, index):
        return self._list.pop(index)

    @property
    def n(self):
        return len(self._list)


class Queue(_QS):
    def pop(self, *args):
        return super(self).pop(0)


class Stack(_QS):
    def pop(self, *args):
        return super(self).pop(-1)



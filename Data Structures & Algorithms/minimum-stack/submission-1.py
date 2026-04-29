class MinStack:
    def __init__(self):
        self._stack = []
        self._min_values = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._min_values) == 0:
            self._min_values.append(val)
        else:
            min_value_so_far = min(val, self._min_values[-1])
            self._min_values.append(min_value_so_far)

    def pop(self) -> None:
        self._stack.pop()
        self._min_values.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_values[-1]

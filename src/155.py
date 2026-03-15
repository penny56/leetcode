class MinStack:

    def __init__(self):
        # 这里的 stack 为 list 类型，其中的元素为 (x, y) tuple类型，其中 x = val, y = min_val
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # 若为空
            self.stack.append((val, val))
        else:
            # 若非空
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

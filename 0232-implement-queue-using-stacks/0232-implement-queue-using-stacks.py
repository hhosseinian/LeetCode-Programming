class MyQueue:

    def __init__(self):
        self.Primary = []

    def push(self, x: int) -> None:
        self.Primary.append(x)

    def pop(self) -> int:
        return self.Primary.pop(0)
        

    def peek(self) -> int:
        return self.Primary[0]
        

    def empty(self) -> bool:
        return len(self.Primary) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
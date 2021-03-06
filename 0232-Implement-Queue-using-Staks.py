class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackIn = []
        self.stackOut = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackIn.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.stackOut.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.stackOut[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.stackIn) and (not self.stackOut)
    
    def move(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

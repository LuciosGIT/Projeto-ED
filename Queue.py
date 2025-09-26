from Node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    
    def dequeue(self):
        if not self.first:
            return None
        data = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
        return data
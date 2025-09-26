from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current.data
            current = current.next
        return None
    
    def __repr__(self):
        
    
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
    
    def values(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print(ll)  # 10 -> 20 -> 30

print(ll.search(20))  # 20
print(ll.search(40))  # None

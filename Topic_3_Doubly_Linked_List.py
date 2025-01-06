# Topic 3: Implement Doubly Linked List with Predefined Input
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    input_values = [5, 10, 15, 20, 25]
    print("Adding values to the doubly linked list:", input_values)
    for val in input_values:
        dll.append(val)
    print("Doubly Linked List:")
    dll.display()

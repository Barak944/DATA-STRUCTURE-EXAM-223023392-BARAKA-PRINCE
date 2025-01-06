# Topic 5: Use Queue to Track Data Dynamically with Predefined Input
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty."

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)

if __name__ == "__main__":
    q = Queue()
    input_values = [10, 20, 30, 40, 50]
    print("Enqueuing values into the queue:", input_values)
    for val in input_values:
        q.enqueue(val)
    print("Queue contents:")
    q.display()
    print("Dequeuing elements:")
    while not q.is_empty():
        print(q.dequeue())
    print("Queue is now empty.")

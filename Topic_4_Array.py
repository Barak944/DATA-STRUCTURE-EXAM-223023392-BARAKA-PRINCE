# Topic 4: Create Array to Manage Fixed Number of Orders with Predefined Input
class FixedArray:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            print("Index out of bounds.")

    def display(self):
        print(self.array)

if __name__ == "__main__":
    size = 5
    fa = FixedArray(size)
    input_values = [(0, 100), (1, 200), (2, 300), (3, 400), (4, 500)]
    print("Inserting values into the fixed array:", input_values)
    for index, value in input_values:
        fa.insert(index, value)
    print("Fixed Array:")
    fa.display()

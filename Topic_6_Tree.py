# Topic 6: Implement a Tree to Represent Hierarchical Data with Predefined Input
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 2, self.data)
        for child in self.children:
            child.display(level + 1)

if __name__ == "__main__":
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    grandchild1 = TreeNode("Grandchild 1")
    grandchild2 = TreeNode("Grandchild 2")
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(grandchild1)
    child2.add_child(grandchild2)
    print("Displaying hierarchical tree structure:")
    root.display()

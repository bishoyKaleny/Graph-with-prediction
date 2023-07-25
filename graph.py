class TreeNode:
    def __init__(self, data,prediction,is_goal=False): #need to edit the prediction so it can be automaticaly the right prediction
        self.data = data
        self.children = []

    def add_child(self, child):
        if isinstance(child, TreeNode):
            self.children.append(child)
        else:
            raise TypeError("Child must be a TreeNode")

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
        else:
            raise ValueError("Child not found")

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def __str__(self, level=0):
        ret = "\t" * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


# Example usage:
if __name__ == "__main__":
    # Create the tree structure
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")
    child1_1 = TreeNode("Child 1.1")
    child1_2 = TreeNode("Child 1.2")
    child2_1 = TreeNode("Child 2.1")

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    child1.add_child(child1_1)
    child1.add_child(child1_2)

    child2.add_child(child2_1)

    # Print the tree
    print("Tree structure:")
    print(root)

    
        
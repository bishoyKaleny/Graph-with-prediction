class TreeNode:
    def __init__(self, data,prediction,is_goal=False): #need to edit the prediction so it can be automaticaly the right prediction
        self.data = data
        self.prediction=prediction
        self.children = []

    def add_child(self, child): #adding child
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
        ret = "\t" * level + repr(self.data)+repr(self.prediction)+ "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def __str__(self, level=0):
        ret = "\t" * level + str(self.data) +"\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def get_prediction_childeren(self):
        '''
        This method is to find the predictions of the childeren of a specific node in order to
        be used in the implementation of the algorithm since you can see the predictions of the node
        that you visited and its childeren
        '''
        node_prediction=self.prediction
        hash_predictions={f'{self.data}':self.prediction}
        for child in self.children:
            hash_predictions[child.data]=child.prediction
        return hash_predictions
            
# Example usage:
if __name__ == "__main__":
    # Create the tree structure
    root = TreeNode("Root",6)
    child1 = TreeNode("Child 1",7)
    child2 = TreeNode("Child 2",2)
    child3 = TreeNode("Child 3",4)
    child1_1 = TreeNode("Child 1.1",5)
    child1_2 = TreeNode("Child 1.2",3)
    child2_1 = TreeNode("Child 2.1",2)

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    child1.add_child(child1_1)
    child1.add_child(child1_2)

    child2.add_child(child2_1)

    # Print the tree
    print("Tree structure:")
    print(root)
    print(root.get_prediction_childeren())

    
        
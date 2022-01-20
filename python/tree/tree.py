class Node():
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.left = None
        self.right = None
    def add_node(self, node):
        if self.value == node.value:
            self.count +=1
        elif self.value > node.value:
            if self.right == None:
                self.right = node
            elif self.right.value > node.value:
                temp_node = self.right
                self.right = node
                self.right.add_node(temp_node)
            else:
                self.right.add_node(node)
        elif self.value < node.value:
            if self.left == None:
                self.left = node
            elif self.left.value < node.value:
                temp_node = self.left
                self.left = node
                self.left.add_node(temp_node)
            else:
                self.left.add_node(node)
                

data_queue = None
test_data = [3,6,2,9,3,6,1]
root = Node(test_data[0])
if __name__ == '__main__':
    for td in test_data[1:]:
        root.add_node(Node(td))




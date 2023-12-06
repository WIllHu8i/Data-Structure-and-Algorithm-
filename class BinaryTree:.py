class BinaryTree:
    def __init__(self,root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        new_node = BinaryTree(new_node)
        if self.left_child is None:
            self.left_child = new_node
        else:
            temp = self.left_child
            self.left_child = new_node
            new_node.left_child = temp
    
    def insert_right(self, new_node):
        new_node = BinaryTree(new_node)
        if self.right_child is None:
            self.right_child = new_node
        else:
            temp = self.right_child
            self.right_child = new_node
            new_node.right_child = temp
    def get_root_val(self):
        return self.key
    
    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    



def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)
def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)
def inorder(tree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)
a_tree = BinaryTree("a")
a_tree.left_child = BinaryTree("b")
a_tree.left_child.right_child = BinaryTree("d")
a_tree.right_child = BinaryTree("c")
a_tree.right_child.left_child = BinaryTree("e")
a_tree.right_child.right_child = BinaryTree("f")
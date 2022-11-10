class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key == None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is found")
            return

        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found!!")

        if self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found!!")

    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):

        if self.lchild:
            self.lchild.inorder()

        print(self.key)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()

        if self.rchild:
            self.rchild.postorder()
        print(self.key)


root = BST(10)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(3)
root.insert(2)
root.insert(1)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(50)

print("Preorder")
root.preorder()

print("Inorder")
root.inorder()

print("Postorder")
root.postorder()

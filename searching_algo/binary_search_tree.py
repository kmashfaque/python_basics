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


root = BST(10)

root.insert(20)
root.insert(30)
root.insert(40)
root.insert(50)

root.search(100)

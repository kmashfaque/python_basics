class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList2:
    def __init__(self):
        self.head = None

    def print_LL2(self):

        if self.head == None:
            print("The linked list is empty!")
        else:
            n = self.head

            while n is not None:
                print(n.data, "---->", end="")
                n = n.ref

    def add_begin2(self, data):

        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end2(self, data):
        new_node = Node(data)
        n = self.head
        if self.head is None:
            self.head = new_node

        while n.ref is not None:
            n = n.ref
        new_node.ref = n.ref
        n.ref = new_node


LL1 = LinkedList2()
LL1.add_begin2(10)
LL1.add_begin2(20)
LL1.add_begin2(30)
LL1.add_end2(40)
LL1.add_end2(50)

LL1.print_LL2()

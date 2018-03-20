# Binary Search Tree in Python

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.value) + '-'+str(self.leftChild) +'-'+ str(self.rightChild)


    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()


    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def lboundary(self):
        if self:
            if self.leftChild:
                print(self.value)
                self.leftChild.lboundary()
            else:
                # dont print if leaf
                if self.leftChild and self.rightChild:
                    print(self.value)

    def leafs(self):
        if self:
            if self.leftChild:
                self.leftChild.leafs()
            if self.leftChild is None and self.rightChild is None :
                print(self.value)
            if self.rightChild:
                self.rightChild.leafs()

    def rboundary(self):
        if self:
            if self.rightChild:
                #print(self.value)
                self.rightChild.rboundary()
            else:
                 # dont print if leaf
                if self.leftChild and self.rightChild:
                    print(self.value)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def preorder(self):
        if self.root is not None:
            print("PreOrder")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("PostOrder")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()

    def boundary(self):
        if self.root is not None:
            print("Boundary")
            self.root.lboundary()
            self.root.leafs()
            self.root.rboundary()
            # self.root.lefts()
            # # print all lefts
            # self.root.leafs()
            # self.root.rights()



def main():
    bst = Tree()
    for i in [20,8,22,4,12,10,14,25, 27]:
        bst.insert(i)
    #bst.insert(7)
    # bst.preorder()
    # bst.postorder()
    # bst.inorder()
    bst.boundary()

main()
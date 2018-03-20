# lis = [10, 12, 10, 15, -1, 7, 6,5, 4, 2, 1, 1, 1]

# target = 11

# res = []
# for key, value in enumerate(lis):
#     cmp_lis = lis[key+1:]
#     for j in cmp_lis:
#         if value + j == target:
#             res.append([value, j])

# print(res)
# print(len(res))
#     #print(value, cmp_lis)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def preorder(self):
        if self.root is not None:
            print("Inorder")
            self.root.preorder()

    def postorder(self):
        if self.root is not None:
            print("postorder")
            self.root.postorder()

    def inorder(self):
        if self.root is not None:
            print("inorder")
            self.root.inorder()


class Node:
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None


    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.left_child:
                self.left_child.insert(data)
                return True
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                self.right_child.insert(data)
                return True
            else:
                self.right_child = Node(data)
                return True

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left_child:
                self.left_child.preorder()

            if self.right_child:
                self.right_child.preorder()

    def postorder(self):
         if self:
            if self.left_child:
                self.left_child.postorder()

            if self.right_child:
                self.right_child.postorder()

            print(str(self.value))

    def inorder(self):
         if self:
            if self.left_child:
                self.left_child.inorder()

            print(str(self.value))

            if self.right_child:
                self.right_child.inorder()




# bst = Tree()
# for i in [1,2,3,4,5]:
#     bst.insert(i)

# bst.preorder()
st = "abhishek"
print(st.reverse())



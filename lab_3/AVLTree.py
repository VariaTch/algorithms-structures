from queue import Queue

q = Queue


class AVLnode:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    # высота определенного узла
    def height(self, AVLNode):
        if AVLNode is None:
            return 0
        else:
            return AVLNode.height

    # вычисление коэффицента балансировки
    def balance(self, AVLNode):
        if AVLNode is None:
            return 0
        else:
            return self.height(AVLNode.left) - self.height(AVLNode.right)

    # поиск пустого узла
    def MinimumValueNode(self, AVLNode):
        if AVLNode is None or AVLNode.left is None:
            return AVLNode
        else:
            return self.MinimumValueNode(AVLNode.left)

    # поворот вправо
    def rotateR(self, AVLNode):
        a = AVLNode.left
        b = a.right
        a.right = AVLNode
        AVLNode.left = b
        AVLNode.height = 1 + max(self.height(AVLNode.left), self.height(AVLNode.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    # поворот влево
    def rotateL(self, AVLNode):
        a = AVLNode.right
        b = a.left
        a.left = AVLNode
        AVLNode.right = b
        AVLNode.height = 1 + max(self.height(AVLNode.left), self.height(AVLNode.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    # вставка
    def insert(self, val, root):
        if root is None:
            return AVLnode(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    # прямой (Preorder) обход дерева
    def DFS_preOrder(self, root):
        if root is None:
            return
        print(root.value)
        self.DFS_preOrder(root.left)
        self.DFS_preOrder(root.right)

    # центрированный (Inorder) обход дерева
    def DFS_inOrder(self, root):
        if root is None:
            return

        self.DFS_inOrder(root.left)
        print(root.value)
        self.DFS_inOrder(root.right)

    # обратный (postOrder) обход дерева
    def DFS_postOrder(self, root):
        if root is None:
            return

        self.DFS_postOrder(root.left)
        self.DFS_postOrder(root.right)
        print(root.value)

    # BFS
    def levelOrder(self, root):
        if root is None:
            return
        else:
            customQueue = q
            customQueue.push(root)
            while not (customQueue.isEmpty()):
                root_1 = customQueue.pop()
                print(root_1.value.data)
                if root_1.value.left is not None:
                    customQueue.push(root_1.value.left)
                if root_1.value.right is not None:
                    customQueue.push(root_1.value.right)

    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.value:
            Node.left = self.delete(val, Node.left)
        elif val > Node.value:
            Node.right = self.delete(val, Node.right)
        else:
            if Node.left is None:
                lt = Node.right
                Node = None
                return lt
            elif Node.right is None:
                lt = Node.left
                Node = None
                return lt
            rgt = self.MinimumValueNode(Node.right)
            Node.value = rgt.value
            Node.right = self.delete(rgt.value, Node.right)
        if Node is None:
            return Node
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        balance = self.balance(Node)
        if balance > 1 and self.balance(Node.left) >= 0:
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) <= 0:
            return self.rotateL(Node)
        if balance > 1 and self.balance(Node.left) < 0:
            Node.left = self.rotateL(Node.left)
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) > 0:
            Node.right = self.rotateR(Node.right)
            return self.rotateL(Node)
        return Node

    def show_wide_tree(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

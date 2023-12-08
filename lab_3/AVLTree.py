from queue import Queue

q = Queue

output_debug = False


def debug(msg):
    if output_debug:
        print(msg)


class AVLnode:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None


class AVL:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0


        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    # высота определенного узла
    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    # поиск пустого узла
    def MinimumValueNode(self, AVLNode):
        if AVLNode is None or AVLNode.left is None:
            return AVLNode
        else:
            return self.MinimumValueNode(AVLNode.left)

    # поворот вправо
    def rotateR(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.value) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

        # поворот влево

    def rotateL(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.value) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

        # вставка

    def insert(self, value):
        tree = self.node

        new_node = AVLnode(value)

        if tree is None:
            self.node = new_node
            self.node.left = AVL()
            self.node.right = AVL()
            debug("Inserted value [" + str(value) + "]")

        elif value < tree.value:
            self.node.left.insert(value)

        elif value > tree.value:
            self.node.right.insert(value)

        else:
            debug("value [" + str(value) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()
                    self.update_heights()
                    self.update_balances()
                self.rotateR()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()
                    self.update_heights()
                    self.update_balances()
                self.rotateL()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    # прямой (Preorder) обход дерева
    def DFS_preOrder(self, node):
        if self.node is None:
            return
        print(self.node.value)
        self.DFS_preOrder(node.left)
        self.DFS_preOrder(node.right)

    # центрированный (Inorder) обход дерева
    def DFS_inOrder(self, node):
        if self.node is None:
            return

        self.DFS_inOrder(node.left)
        print(self.node.value)
        self.DFS_inOrder(node.right)

    # обратный (postOrder) обход дерева
    def DFS_postOrder(self, node):
        if self.node is None:
            return

        self.DFS_postOrder(node.left)
        self.DFS_postOrder(node.right)
        print(self.node.value)

    # BFS
    def levelOrder(self, node):
        if self.node is None:
            return
        else:
            customQueue = q
            customQueue.push(self.node)
            while not (customQueue.isEmpty()):
                root_1 = customQueue.pop()
                print(root_1.value.data)
                if root_1.value.left is not None:
                    customQueue.push(root_1.value.left)
                if root_1.value.right is not None:
                    customQueue.push(root_1.value.right)

    def delete(self, value):
        if self.node is not None:
            if self.node.value == value:
                debug("Deleting ... " + str(value))
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node

                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        debug("Found replacement for " + str(value) + " -> " + str(replacement.value))
                        self.node.value = replacement.value

                        self.node.right.delete(replacement.value)

                self.rebalance()
                return
            elif value < self.node.value:
                self.node.left.delete(value)
            elif value > self.node.value:
                self.node.right.delete(value)

            self.rebalance()
        else:
            return

    def is_leaf(self):
        return self.height == 0

        # Find the smallest valued node in RIGHT child

    def logical_successor(self, node):
        node = node.right.node
        if node is not None:
            while node.left is not None:
                debug("LS: traversing: " + str(node.value))
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def display(self, level=0, pref=''):
        self.update_heights()
        self.update_balances()
        if self.node is not None:
            print('-' * level * 2, pref, self.node.value, "[" + str(self.height) + ":" + str(self.balance) + "]",
                  'Leaf' if self.is_leaf() else ' ')
            self.node.left.display(level + 1, '>')
            if self.node.left is not None:
                self.node.right.display(level + 1, '>')

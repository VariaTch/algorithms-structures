class BinNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    # добавление значений в дерево

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    # отображение дерева
    def show_tree(self, node):
        if node is None:
            return
        print(node.data)
        self.show_tree(node.left)

        self.show_tree(node.right)


    def show_wide_tree(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn +=[x.left]
                if x.right:
                    vn+=[x.right]
            print()
            v = vn

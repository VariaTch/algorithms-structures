from BinaryTree import BinNode, Tree
from AVLTree import AVLnode, AVL


def AVLFromBin(binaryRoot, avlTree):
    if binaryRoot:
        avlTree.insert(binaryRoot.data)
        AVLFromBin(binaryRoot.right, avlTree)
        AVLFromBin(binaryRoot.left, avlTree)


def correct_parentheses(s):
    start = -1
    count_left = 0
    count_right = 0

    while True:
        start = s.find("(", start + 1)
        if start == -1:
            break
        count_left += 1

    while True:
        start = s.find(")", start + 1)
        if start == -1:
            break
        count_right += 1

    if count_left == count_right:
        return True


def positive_numbers(s):
    try:
        if '-' in s:
            print("Вы ввели отрицательные числа")

            return False
        else:
            return True
    except Exception as e:
        print(e)


def read_file():
    file1 = open("test.txt", "r")

    while True:
        # считываем строку
        s = file1.readline()
        # прерываем цикл, если строка пустая
        if not s:
            break
        s = s.strip()

        if correct_parentheses(s):
            res_s = s.replace('(', '')
            res_s = res_s.replace(')', '')
            if positive_numbers(res_s):
                return res_s
            else:
                break
        else:
            print('Неправильные скобки')

    # закрываем файл
    file1.close()


t = Tree()
a_tree = AVL()
res = read_file()
if type(res) == str:
    for x in res:
        t.append(BinNode(x))

    t.show_tree(t.root)

print('______________________________________')
AVLFromBin(t.root, a_tree)
a_tree.display()

print('In_order: ', a_tree.inorder_traverse())
print('Pre_order: ', a_tree.preorder_traverse())
print('Post_order: ', a_tree.postorder_traverse())
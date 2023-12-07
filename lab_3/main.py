from BinaryTree import BinNode, Tree
from AVLTree import AVLnode, AVL


# s = "(8(9(5))(1))"


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
        # выводим строку
        print(s.strip())
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

    t.show_wide_tree(t.root)

print('______________________________________')
rt = None
if type(res) == str:
    for x in res:
        a_tree.insert(int(x), rt)

#rt = None
#rt = Tree.insert(3, rt)
a_tree.DFS_preOrder(rt)
print('______________________________________')
a_tree.DFS_inOrder(rt)
print('______________________________________')
a_tree.DFS_postOrder(rt)
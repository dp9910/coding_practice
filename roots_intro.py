##understanding roots####


from signal import valid_signals
from tabnanny import check


class TreeNode:

    def __init__(self,val):

        self.val = val
        self.left=None
        self.right=None

    def is_left_filled(self):

        return self.left is not None
    
    def is_right_filled(self):

        return self.right is not None
    
    def count_nodes(self):

        left_count = 0 if self.left is None else self.left.count_nodes()
        right_count = 0 if self.right is None else self.right.count_nodes()

        return 1+ left_count + right_count



root=TreeNode(3)
root.left = TreeNode(3)
root.right=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

print(root.left.val)

print(root.left.right.val)

print(TreeNode.is_left_filled(root.left))

print(TreeNode.is_right_filled(root.right))

print(TreeNode.count_nodes(root))
print(root.count_nodes())



###############################################


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



##count all nodes


def count_all_nodes(node):

    if node is None:
        return 0
    return 1 + count_all_nodes(node.left) + count_all_nodes(node.right)


def maximum_height(node):

    if node is None:
        return 0
    max_left = maximum_height(node.left)
    max_right = maximum_height(node.right)

    return 1+max(max_left,max_right)


def check_if_value_exist(node,value):

    if node is None:
        return False
    if node.val==value:
        return True
    return check_if_value_exist(node.left,value) or check_if_value_exist(node.right,value)

root=TreeNode(3)
root.left = TreeNode(3)
root.right=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

print("value there",check_if_value_exist(root,12))
print("max height",maximum_height(root))
print("ct",count_all_nodes(root))




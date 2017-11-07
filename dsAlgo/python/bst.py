class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node

    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

def check_if_bst(root):
    if not root:
        return True
    if(node_max(root.l_child) < root.data <= node_min(root.r_child)) and check_if_bst(root.l_child) and check_if_bst(root.r_child):
        return True
    else:
        return False

def node_max(root):
    if not root:
        return float("-inf")
    maxLeft = node_max(root.l_child)
    maxRight = node_max(root.r_child)
    return max(root.data, maxLeft, maxRight)
def node_min(root):
    if not root:
        return float("inf")
    minLeft = node_min(root.l_child)
    minRight = node_min(root.r_child)
    return min(root.data, minLeft, minRight)

r = Node(3)
binary_insert(r,Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))

print ("in order:")
in_order_print(r)

print ("pre order")
pre_order_print(r)

print("Is bst : %s"%check_if_bst(r))

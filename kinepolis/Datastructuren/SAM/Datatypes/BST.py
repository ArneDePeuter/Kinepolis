
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def searchTreeInsert(self, key,val):
        param = Node(key, val)
        if self.root is None:
            self.root = param
            return True
        else:
            current = self.root
            while current:
                if param.key < current.key:
                    if current.left is None:
                        current.left = param
                        return True
                    else:
                        current = current.left
                elif param.key > current.key:
                    if current.right is None:
                        current.right = param
                        return True
                    else:
                        current = current.right
                elif param.key == current.key:
                    current.val = param.val
                    return True

    def searchTreeRetrieve(self, key):
        if self.root is None:
            return False, False
        else:
            current = self.root
            while current:
                if key < current.key:
                    if current.left is None:
                        return False, False
                    else:
                        current = current.left
                elif key > current.key:
                    if current.right is None:
                        return False, False
                    else:
                        current = current.right
                elif key == current.key:
                    return current.val, True

    def inorderTraverse(self, func):
        def traverseer(node):
            if node is not None:
                traverseer(node.left)
                func(node.key)
                traverseer(node.right)

        traverseer(self.root)

    def searchTreeDelete(self, key):
        if self.root is None:
            return False

        parent = None
        current = self.root

        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        elif current.left is None or current.right is None:
            if current.left is not None:
                child = current.left
            else:
                child = current.right

            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child
        else:
            parent_of_min = current
            min_node = current.right
            while min_node.left is not None:
                parent_of_min = min_node
                min_node = min_node.left

            current.key = min_node.key
            current.val = min_node.val

            if parent_of_min.left == min_node:
                parent_of_min.left = None
            else:
                parent_of_min.right = None

        return True

    def load(self, input_data):
        self.root = None

        def extract_numbers(data):
            if "root" in data:
                root = data["root"]
                self.searchTreeInsert(root)
                if "children" in data:
                    for child in data["children"]:
                        if child:
                            extract_numbers(child)

        extract_numbers(input_data)

    def save(self):
        def helper(node):
            if node is None:
                return None
            left_child = helper(node.left)
            right_child = helper(node.right)
            children = []
            if left_child is not None:
                children.append(left_child)
            if right_child is not None:
                children.append(right_child)
            if children:
                if len(children) == 1:
                    if left_child is None:
                        children = []
                        children.append(None)
                        children.append(right_child)
                    else:
                        children = []
                        children.append(left_child)
                        children.append(None)
                return {"root": node.val, "children": children}
            return {"root": node.val}

        return helper(self.root)

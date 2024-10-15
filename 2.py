class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def find_min_value(node):
    current = node

    while current.left is not None:
        current = current.left
    return current.value


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.right = Node(80)

    print("Найменше значення в дереві:", find_min_value(root))

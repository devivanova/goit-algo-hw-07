class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def find_sum_of_values(node):
    if node is None:
        return 0

    return node.value + find_sum_of_values(node.left) + find_sum_of_values(node.right)


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    print("Сума всіх значень у дереві:", find_sum_of_values(root))

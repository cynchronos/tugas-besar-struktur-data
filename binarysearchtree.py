class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if int(key.sku) < int(root.key.sku):
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, sku):
        return self._search_recursive(self.root, sku)

    def _search_recursive(self, root, sku):
        if root is None or root.key.sku == sku:
            return root
        if sku < root.key.sku:
            return self._search_recursive(root.left, sku)
        return self._search_recursive(root.right, sku)

    def update_stok(self, sku, new_stok):
        node = self.search(sku)
        if node:
            node.key.stok = new_stok
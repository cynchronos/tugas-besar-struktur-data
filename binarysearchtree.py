class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class StockFunction:
    def __init__(self):
        self.root = None

    def insert(self, key):
        key['no_sku'] = int(key['no_sku'])
        root = self.root if self.root is None else None
        if root is None:
            self.root = Node(key)
        else:
            self._insert(key, root)

    def _insert(self, key, node):
        key['no_sku'] = key['no_sku']
        if key["no_sku"] < node.key["no_sku"]:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        elif key["no_sku"] > node.key["no_sku"]:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)
        else:
            return key

    def findAll(self):
        new_node = Node(None)
        if self.root:
            result = []

            stack = []
            root = self.root

            while root or stack:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()

                    result.append(root.key)

                    root = root.right
            return result
        else:
            self.root = new_node

    def findOne(self, query, value, root=None):
        value = int(value)
        new_node = Node(value)
        root = self.root if root is None else root
        if root:
            if root.key[query] == value:
                return root.key
            elif root.key[query] < value:
                if root.right is None:
                    return None
                return self.findOne(query, value, root.right)
            elif root.key[query] > value:
                if root.left is None:
                    return None
                return self.findOne(query, value, root.left)
            else:
                return None
        else:
            self.root = new_node
            
    def update(self, query, value, data, root=None):
        value = int(value)
        new_node = Node(value)
        root = self.root if root is None else root

        if root:
            if root.key[query] == value:
                for index in data.keys():
                    root.key[index] = data[index]
                return True
            elif root.key[query] < value:
                if root.right is None:
                    return None
                return self.update(query, value, root.right)
            elif root.key[query] > value:
                if root.left is None:
                    return None
                return self.update(query, value, root.left)
            else:
                self.root = new_node

    # def delete(self, key):
    #     if self.root:
    #         self.root = self._delete(key, self.root)

    # def _delete(self, key, node):
    #     if node is None:
    #         return node
    #     if key["no_sku"] < node.key["no_sku"]:
    #         node.left = self._delete(key)


class TransactionFunction:
    data = []

    def insert(self, key):
        self.data.append(key)

    def insertMany(self, keys):
        for key in keys:
            self.data.append(key)

    def findAll(self):
        if len(self.data) != 0:
            return self.data.copy()
        else:
            return None

    def findOne(self, query, value):
        if len(self.data) != 0:
            for data in self.data:
                if data[query] == value:
                    return data.copy()
        else:
            return None

    # def update(self, key, data):
    #     if len(self.data) != 0:
    #         self.data[key] = data
    #     else:
    #         return "Data Kosong"

Stock = StockFunction()
Transaction = TransactionFunction()
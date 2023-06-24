class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# create bst crud Stok without validation
class Stock:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key['no_sku'] < node.key['no_sku']:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        elif key['no_sku'] > node.key['no_sku']:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)
        else:
            print('key is already in tree')

    def findAll(self):
        if self.root:
            result = []
            
            stack = []
            node = self.root
            
            while node or stack:
                if node:
                     stack.append(node)
                     node = node.left
                else:
                    node = stack.pop()
                    
                    result.append(node.key)

                    node = node.right
            return result
        else:
            return None
    
    def findOne(self, query, value, root=None):
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
        
    # def inorder(self):
    #     if self.root:
    #         self._inorder(self.root)

    # def _inorder(self, node):
    #     if node:
    #         self._inorder(node.left)
    #         print(node.key)
    #         self._inorder(node.right)

    # def preorder(self):
    #     if self.root:
    #         self._preorder(self.root)

    # def _preorder(self, node):
    #     if node:
    #         print(node.key)
    #         self._preorder(node.left)
    #         self._preorder(node.right)

    # def postorder(self):
    #     if self.root:
    #         self._postorder(self.root)

    # def _postorder(self, node):
    #     if node:
    #         self._postorder(node.left)
    #         self._postorder(node.right)
    #         print(node.key)
    
    # def update_by_sku(self, key, data):
    #     if self.root is None:
    #          self.root = Node(key)
    #     else:
    #         self._update_by_sku(key, data, self.root)
    
    # def _update_by_sku(self, key, data, node):
    #     if node is None:
    #         return node
    #     if key['no_sku'] < node.key['no_sku']:
    #         node.left = self._update_by_sku(key, data, node.left)
    #     elif key['no_sku'] > node.key['no_sku']:
    #         node.right = self._update_by_sku(key, data, node.right)
    #     else:
    #         node.key = data
    #     return node

    def delete(self, key):
        if self.root:
            self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return node
        if key['no_sku'] < node.key['no_sku']:
            node.left = self._delete(key)
            
class Transaction:
    
    data = []
    
    def insert(self, key):
        self.data.append(key)
    
    def findAll(self):
        if len(self.data) != 0:
            return self.data
        else:
            return "Data Kosong"
    
    def findOne(self, query, value):
        if len(self.data) != 0:
            for i in self.data:
                if i[query] == value:
                    return i
        else:
            return "Data Kosong"
    
    # def update(self, key, data):
    #     if len(self.data) != 0:
    #         self.data[key] = data
    #     else:
    #         return "Data Kosong"
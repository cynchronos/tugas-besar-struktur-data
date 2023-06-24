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


class DataTransaksi:
    def __init__(self, sku, nama, harga, stok):
        self.sku = sku
        self.nama = nama
        self.harga = harga
        self.stok = stok


def tambah_data_transaksi():
    nama_konsumen = input("Masukkan Nama Konsumen: ")
    transaksi = []
    while True:
        sku = input("Masukkan No. SKU barang yang dibeli: ")
        jumlah_beli = int(input("Masukkan Jumlah Beli: "))

        node = bst.search(sku)
        if node:
            if node.key.stok >= jumlah_beli:
                subtotal = node.key.harga * jumlah_beli
                node.key.stok -= jumlah_beli
                transaksi.append((nama_konsumen, node.key.sku, jumlah_beli, subtotal))
                print("Data Transaksi Konsumen Berhasil Diinputkan")
                lanjut = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? ")
                if lanjut.upper() == 'N':
                    break
            else:
                print("Jumlah Stok No. SKU yang Anda beli tidak mencukupi")
                lanjut = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
                if lanjut.upper() == 'N':
                    break
        else:
            print("No. SKU yang diinputkan belum terdaftar")
            lanjut = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
            if lanjut.upper() == 'N':
                break

    return transaksi


bst = BinarySearchTree()  # Inisialisasi BST dengan barang-barang

# Contoh inisialisasi data barang
barang1 = DataTransaksi("5521", "farhan", 50000, 10)
barang2 = DataTransaksi("1234", "kamal", 70000, 5)

bst.insert(barang1)
bst.insert(barang2)

transaksi = tambah_data_transaksi()

# Cetak data transaksi
for data in transaksi:
    print("Nama Konsumen:", data[0])
    print("No. SKU:", data[1])
    print("Jumlah Beli:", data[2])
    print("Subtotal:", data[3])
    print()
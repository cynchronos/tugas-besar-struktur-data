from binarysearchtree import Stock
# Fungsi untuk melakukan restok barang
def restok_barang():
    sku = input("Masukkan No. SKU barang: ")
    node = Stock.findOne("no_sku", sku) 

    if node is not None:
        stok_baru = int(input("Masukkan jumlah stok baru: "))
        node['jumlah_stok'] += stok_baru
        Stock.update("no_sku", sku, node)
        print("Stok barang telah berhasil diperbarui menjadi:", node['jumlah_stok'])
    else:
        print("No. SKU tidak ditemukan.")

# Inisialisasi data barang pada BST
Stock.insert({'no_sku' : '1234', 'nama_barang' : 'Karbu', 'harga_satuan': 150000, 'jumlah_stok' : 10})
Stock.insert({'no_sku' : '4567', 'nama_barang' : 'Laptop', 'harga_satuan': 2000000, 'jumlah_stok' : 60})
Stock.insert({'no_sku' : '9999', 'nama_barang' : 'Keyboard', 'harga_satuan': 270000, 'jumlah_stok' : 35})
# Memanggil fungsi restok_barang
restok_barang()
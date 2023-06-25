from binarysearchtree import Stock
# Fungsi untuk melakukan restok barang
def restok_barang():
    sku = input("Masukkan No. SKU barang: ")
    node = Stock.findOne("no_sku", sku) 

    if node is not None:
        stok_baru = int(input("Masukkan jumlah stok baru: "))
        node['jumlah_stok'] += stok_baru
        Stock.update("no_sku", sku, node)
        return print("Stok barang telah berhasil diperbarui:\n",node)
    else:
        return print("No. SKU tidak ditemukan.")